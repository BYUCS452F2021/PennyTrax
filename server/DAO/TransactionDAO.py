from database import Database


class TransactionDAO:
    def __init__(self):
        self.db = Database()

    def get_transactions(self, id=None):
        return dummy_transactions

    def add_transaction(self, transaction):
        cursor = self.db.connection.cursor()
        sql = (
            "INSERT INTO Transaction VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        values = (transaction.id,
                  transaction.account_id,
                  transaction.date,
                  transaction.amount,
                  transaction.pending,
                  transaction.merchant_name,
                  transaction.description,
                  transaction.category,
                  transaction.notes,
                  transaction.split,
                  transaction.parent_transaction_id,
                  transaction.hidden_from_budget)
        cursor.execute(sql, values)
        self.db.connection.commit()
        cursor.close()

    def import_transactions(self, transactions):
        cursor = self.db.connection.cursor()
        for transaction in transactions:
            sql = (
                "INSERT INTO Transaction VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
            values = (transaction["id"],
                      transaction["account_id"],
                      transaction["date"],
                      transaction["amount"],
                      transaction["pending"],
                      transaction["merchant_name"],
                      transaction["description"],
                      transaction["category"],
                      transaction["notes"],
                      transaction["split"],
                      transaction["parent_transaction_id"],
                      transaction["hidden_from_budget"])
            cursor.execute(sql, values)
            print("inserted: " + str(transaction["id"]))

        self.db.connection.commit()
        cursor.close()
        print("complete")


dummy_transactions = [
    {
        "id": "3jNnEDA5WefVqGW59Eo5Fg45dB33o5FqXoQ3w",
        "account_id": 101,
        "date": "2021-01-25",
        "amount": 25300,
        "pending": False,
        "merchant_name": "United Airlines",
        "description": "United Airlines",
        "category": "Travel",
        "notes": "",
        "split": False,
        "hidden_from_budget": False
    },
    {
        "id": "qrQJZaykmEtm7XzgGb9gTnzkrK7kAvudxbLw6",
        "account_id": 101,
        "date": "2021-01-27",
        "amount": 700,
        "pending": False,
        "merchant_name": "KFC",
        "description": "KCF",
        "category": "Fast Food",
        "notes": "",
        "split": False,
        "hidden_from_budget": False
    },
    {
        "id": "mRPMjBnxepiWwV317Lr1IeDJny8Mb4HLBKAQj",
        "account_id": 101,
        "date": "2021-01-29",
        "amount": 300000,
        "pending": False,
        "merchant_name": "BYU",
        "description": "Tuition",
        "category": "Education",
        "notes": "",
        "split": False,
        "hidden_from_budget": False
    }
]
