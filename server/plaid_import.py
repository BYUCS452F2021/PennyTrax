import plaid
from DAO import TransactionDAO

# Imports transactions from plaid and adds or updates them in the Transactions table
async def import_transactions():
    at = "access-sandbox-50ff7ceb-ebdc-40e8-ae22-27146fb1bed4"
    start = "2021-01-01"
    end = "2021-01-30"
    plaid_trans = await plaid.get_transactions(at, start, end)
    transactions = []

    # Convert plaid transaction model to pennytrax model
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
