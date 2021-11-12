import plaid
from DAO import AccountDAO
from DAO import TransactionDAO

# Imports transactions and account balances from plaid and adds or updates them in the Transaction and FinancialAccount table

async def import_transactions(access_token):
    start = "2021-01-01"
    end = "2021-01-30"
    plaid_trans = await plaid.get_transactions(access_token, start, end)
    print(plaid_trans)

    # Convert plaid account model to pennytrax model
    accounts = []
    for account in plaid_trans["accounts"]:
        accounts.append({
            "id": account["account_id"],
            "available_balance": account["balances"]["available"],
            "current_balance": account["balances"]["current"],
        })

    # Update accounts in the database
    account_dao = AccountDAO()
    account_dao.update_accounts(accounts)

    # Convert plaid transaction model to pennytrax model
    transactions = []
    for tran in plaid_trans["transactions"]:
        transactions.append({
            "id": tran["transaction_id"],
            "account_id": tran["account_id"],
            "date": tran["date"],
            "amount": tran["amount"],
            "pending": tran["pending"],
            "merchant_name": tran["merchant_name"],
            "description": tran["name"],
            "category": tran["category"][0],
            "notes": "",
            "split": False,
            "parent_transaction_id": "",
            "hidden_from_budget": False
        })

    # Add transactions to the database
    dao = TransactionDAO()
    dao.import_transactions(transactions)
    return transactions
