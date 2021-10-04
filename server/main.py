#! /usr/bin/env python3
from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import DAO.UserDAO as userDAO
from DAO.AccountDAO import AccountDAO
import data_models
import plaid
import link

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


@app.get("/user/{user_id}")
async def read_user(user_id):
    return userDAO.read_user(int(user_id))

@app.get("/accounts")
async def get_accounts():
    dao = AccountDAO()
    return dao.get_accounts()

@app.get("/accounts/{id}")
async def get_account(id):
    dao = AccountDAO()
    return dao.get_accounts(id=int(id))

# NOTE: make sure you're including the header "Content-Type: application/json"
@app.post("/accounts/add")
async def add_account(account: data_models.Account):
    dao = AccountDAO()
    # TODO: data validation to make sure this account is valid.
    acct_id = dao.add_account(account)
    return {"account_id": acct_id}

""" To test this on the terminal:

curl localhost:8000/accounts/add -H "Content-Type: application/json" -d \
'{"id": 3,"financial_institution_id": "ghi123","user_id": "demo_user","name": "Savings","type": "depository","subtype": "savings","available_balance": "2500","current_balance": "2500"}'
    
"""

@app.post("/institutions/add")
async def add_institution():
    token = await plaid.get_link_token(user='test user') # Not sure how to handle user yet.
    # TODO: replace with real IP
    url = "localhost:8000/link/begin/" + token
    # Do we need to try to obfuscate the token at all?
    return {
        "link_url": url
    }

@app.get("/link/begin/{link_token}")
async def begin_link(link_token: str):
    """Returns HTML content to be viewed in a web browser:
    A page where the end-user can sign in to a supported financial institution.
    """
    # TODO: get user auth token from http headers
    # determine the user id from that token
    user_id = 101
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
    # TODO: store the user id & access token in the FinancialInstitutions table

    # Maybe kick off a download process of transactions using this new access token,
    # and fill the database with them?

    # Note: use plaid.get_transactions(access_token, start, end)



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



if __name__ == "__main__":
    # You can just run ./main.py to start the API now
    # (or python3 main.py if your interpreter is giving you trouble)
    uvicorn.run("main:app", port=8000, reload=True)