from mongo_database import MongoDatabase
from bson.objectid import ObjectId


class TransactionDAO:
    def __init__(self):
        self.db = MongoDatabase().db

    # Returns all transactions that have an account_id in the account_ids param
    def get_transactions(self, account_ids: list):
        if len(account_ids) == 0:
            return []

        transactions = []
        for account_id in account_ids:
            for transaction in self.db.transaction.find({"account_id": account_id}):
                transaction["id"] = str(transaction["_id"])
                del transaction["_id"]
                transactions.append(transaction)
        return transactions

    def add_transaction(self, transaction):
        result = self.db.transaction.insert_one(transaction)
        return str(result.inserted_id)

    def import_transactions(self, transactions):
        result = self.db.transaction.insert_many(transactions)
        return str(result.inserted_ids)

    def update_transaction(self, transaction):
        filter = {'id': transaction.id}
        newvalues = {"$set": {'date': transaction.date,
                              "amount": transaction.amount,
                              "pending": int(transaction.pending),
                              "merchant_name": transaction.merchant_name,
                              "description": transaction.description,
                              "category": transaction.category,
                              "notes": transaction.notes,
                              "split": int(transaction.split),
                              "parent_transaction_id": transaction.parent_transaction_id,
                              "hidden_from_budget": transaction.hidden_from_budget
                              }}

        transaction.date,
        transaction.amount,
        int(transaction.pending),
        transaction.merchant_name,
        transaction.description,
        transaction.category,
        transaction.notes,
        int(transaction.split),
        transaction.parent_transaction_id,
        int(transaction.hidden_from_budget)

    def delete_transaction(self, transaction_id):
        self.db.Transaction.delete_one({"transaction_id": transaction_id})
