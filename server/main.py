#! /usr/bin/env python3
import hashlib
import asyncio
import uvicorn
from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
import data_models
import plaid
import link
import plaid_import
import uuid
from DAO import UserDAO, AuthTokenDAO, AccountDAO, TransactionDAO
# TODO: any time you add new DAO's, edit DAO/__init__.py for cleaner imports.

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}

# Accounts:


@app.get("/accounts/{auth_token}")
async def get_accounts(auth_token: str):
    dao = AccountDAO()
    auth_dao = AuthTokenDAO()
    user_id = auth_dao.verify_auth_token(auth_token)
    return dao.get_institutions_accounts(user_id)

# @app.get("/accounts/{id}")
# async def get_account(id):
#     dao = AccountDAO()
#     return dao.get_accounts(id=int(id))

# NOTE: make sure you're including the header "Content-Type: application/json"


@app.post("/accounts/add")
async def add_account(request: data_models.SimpleAccount):
    auth_token_dao = AuthTokenDAO()
    user_id = auth_token_dao.verify_auth_token(request.authToken)

    dao = AccountDAO()
    # TODO: data validation to make sure this account is valid.
    acct_id = dao.add_account({
        "id": "CASH-" + str(uuid.uuid4()),
        "financial_institution_id": None,
        "user_id": user_id,
        "name": request.name,
        "type": "",
        "subtype": "",
        "mask": "0000",
        "available_balance": request.available_balance,
        "current_balance": request.current_balance
    })
    return {"account_id": acct_id}

""" To test this on the terminal:

curl localhost:8000/accounts/add -H "Content-Type: application/json" -d \
'{"id": 3,"financial_institution_id": "ghi123","user_id": "demo_user","name": "Savings","type": "depository","subtype": "savings","available_balance": "2500","current_balance": "2500"}'
    
"""

# Institutions / Linking


@app.post("/institutions/add")
async def add_institution(request: data_models.SimpleRequest):
    auth_token_dao = AuthTokenDAO()
    user_id = auth_token_dao.verify_auth_token(request.authToken)
    # Not sure how to handle user yet.
    token = await plaid.get_link_token(user='test user')
    # TODO: replace with real IP
    url = "localhost:8000/link/begin/" + token + "/" + str(user_id)
    # Do we need to try to obfuscate the token at all?
    return {
        "link_url": url
    }


@app.get("/link/begin/{link_token}/{user_id}")
async def begin_link(link_token: str, user_id: str):
    """Returns HTML content to be viewed in a web browser:
    A page where the end-user can sign in to a supported financial institution.
    """
    # TODO: get user auth token from http headers
    # determine the user id from that token
    html = link.get_link_html(user_id, link_token)
    return Response(content=html)


@app.get("/link/done")
async def link_done_page():
    """Returns HTML content to be viewed in a web browser:
    A landing page that informs the user that the process was successful.
    Ideally this is not shown at all (the front end should realize that
    the browser navigated, and take the user back to the previous page)
    """
    return Response(content=link.get_done_html())


@app.post("/link/store_token")
async def link_store_token(data: data_models.PlaidSignInResult):
    """To be invoked from the HTML sign-in page; this function
    exchanges a public token retrieved from the sign-in page for
    an auth token and stores it in the database with a user ID.
    """
    print("Got Public Token", data.public_token, "for user", data.user_id)
    access_token = await plaid.get_access_token(data.public_token)
    print("Exchanged for Access Token:", access_token)

    # Add financial institution and accounts to database
    dao = AccountDAO()
    financial_institution_id = dao.add_institution(
        data.user_id, data.name, access_token)
    dao.add_institution_accounts(
        data.user_id, financial_institution_id, data.accounts)

    # Import account balances and transactions
    await plaid_import.import_transactions(data.user_id)

    # Note: use plaid.get_transactions(access_token, start, end)

# Transactions

# Demo API endpoint to get transactions. We probably don't actually need to expose
# an endpoint like this since getting transactions from Plaid will happen on the backend,
# but this is here just to show how it's done.
# TODO: delete me :p


@app.get("/test_transactions")
async def transactions_test():
    at = "access-sandbox-50ff7ceb-ebdc-40e8-ae22-27146fb1bed4"
    start = "2021-01-01"
    end = "2021-01-30"
    trans = await plaid.get_transactions(at, start, end)
    return trans


@app.post("/transactions")
async def get_transactions(request: data_models.SimpleRequest):
    auth_token_dao = AuthTokenDAO()
    user_id = auth_token_dao.verify_auth_token(request.authToken)

    # Get list of users accounts
    dao = AccountDAO()
    account_ids = dao.get_account_ids(user_id)

    dao = TransactionDAO()
    return dao.get_transactions(account_ids)


@app.post("/transactions/add")
async def get_transactions(transaction: data_models.Transaction):
    dao = TransactionDAO()
    # TODO: data validation to make sure this account is valid.
    dao.add_transaction(transaction)
    return {"success": True}


@app.delete("/transactions/delete/{transaction_id}")
async def delete_transaction(transaction_id: str):
    dao = TransactionDAO()
    # TODO: data validation to make sure this account is valid.
    dao.delete_transaction(transaction_id)
    return {"success": True}


@app.post("/transactions/import")
async def import_transactions():
    user_id = 125
    await plaid_import.import_transactions(user_id)
    return {"success": True}


@app.post("/transactions/update")
async def update_transaction(transaction: data_models.Transaction):
    dao = TransactionDAO()
    # TODO: data validation to make sure this account is valid.
    dao.update_transaction(transaction)
    return {"success": True}


@app.get("/users/")
async def get_all_users():
    dao = UserDAO()
    return dao.get_all_users()


@app.get("/users/{user_id}")
async def get_user(user_id: int):
    dao = UserDAO()
    return dao.get_user(int(user_id))


@app.post("/register/")
async def register(request: data_models.RegisterRequest):
    dao = UserDAO()
    auth_token_dao = AuthTokenDAO()

    if dao.get_user_by_email(request.email):
        return {"success": False, "message": "Email already exists"}

    salted_pass = request.password + request.salt
    hashed_pass = hashlib.sha256(salted_pass.encode('utf-8')).hexdigest()

    user_id = dao.create_user({
        "first_name": request.first_name,
        "last_name": request.last_name,
        "email": request.email,
        "password": hashed_pass,
        "salt": request.salt
    })
    auth_token = auth_token_dao.create_auth_token(user_id)
    return {"success": True, "auth_token": auth_token}


@app.post("/login/")
async def login(request: data_models.LoginRequest):
    user_dao = UserDAO()
    auth_token_dao = AuthTokenDAO()

    user = user_dao.get_user_by_email(request.email)

    if user == None:
        return {"success": False, "message": "Username does not exist"}

    salted_pass = request.password + user["salt"]
    hashed_pass = hashlib.sha256(salted_pass.encode('utf-8')).hexdigest()

    if user["password"] != hashed_pass:
        return {"success": False, "message": "Password is incorrect"}
    else:
        auth_token = auth_token_dao.create_auth_token(user["id"])

        # Import plaid data in background
        asyncio.create_task(plaid_import.import_transactions(user["id"]))

        return {"success": True, "auth_token": auth_token}


if __name__ == "__main__":
    # You can just run ./main.py to start the API now
    # (or python3 main.py if your interpreter is giving you trouble)
    uvicorn.run("main:app", port=8000, reload=True)
