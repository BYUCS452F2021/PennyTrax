from .config import *
import requests

PLAID_TRANSACTIONS_URL = "https://sandbox.plaid.com/transactions/get"

async def get_transactions(access_token, start_date, end_date, account_ids=None):
    data = {
        "access_token": access_token,
        "start_date": start_date,
        "end_date": end_date,
        "options": {
            "account_ids": account_ids
            # There are more options defined here:
            # https://plaid.com/docs/api/products/
        }
    }
    r = requests.post(PLAID_TRANSACTIONS_URL, headers=STANDARD_PLAID_HEADERS, json=data)
    resp = r.json()
    print("Downloaded", len(resp), "transactions")
    return resp