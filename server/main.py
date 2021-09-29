from fastapi import FastAPI, Request, Response
import DAO.UserDAO as userDAO
from DAO.AccountDAO import AccountDAO
import data_models
import plaid
import link

app = FastAPI()


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
    token = plaid.get_link_token(user='test user') # Not sure how to handle user yet.
    # TODO: replace with real IP
    url = "localhost:8000/link/begin/" + token
    # Do we need to try to obfuscate the token at all?
    return {
        "link_url": url
    }

@app.get("/link/begin/{link_token}")
async def begin_link(link_token: str):
    html = link.get_html(link_token)
    return Response(content=html)

@app.post("/link/complete")
async def complete_link(data: data_models.PlaidSignInResult):
    # TODO: access data.public_token and send it to the PLAID
    # api's for an access token, then store the access token
    # in the FinancialInstitutions table

    # Maybe kick off a download process of transactions 
    # using this new access token.
    pass