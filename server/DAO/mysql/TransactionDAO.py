from mysql_database import MysqlDatabase


class TransactionDAO:
    def __init__(self):
        self.db = MysqlDatabase()

    # Returns all transactions that have an account_id in the account_ids param
    def get_transactions(self, account_ids: list):
        if len(account_ids) == 0:
            return []

        cursor = self.db.connection.cursor()
        format_account_ids = ','.join(['%s'] * len(account_ids))
        cursor.execute("SELECT * FROM Transaction WHERE account_id IN (%s)" %
                       format_account_ids, tuple(account_ids))

        transactions = []
        for transaction in cursor.fetchall():
            transactions.append({
                "id": transaction[0],
                "account_id": transaction[1],
                "date": transaction[2],
                "amount": transaction[3],
                "pending": bool(transaction[4]),
                "merchant_name": transaction[5],
                "description": transaction[6],
                "category": transaction[7],
                "notes": transaction[8],
                "split": bool(transaction[9]),
                "parent_transaction_id": transaction[10],
                "hidden_from_budget": bool(transaction[11])
            })

        return transactions

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
                "INSERT INTO Transaction VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE pending = %s;")
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
                      transaction["hidden_from_budget"],
                      # Update the following on duplicate key
                      transaction["pending"])

            cursor.execute(sql, values)

        self.db.connection.commit()
        cursor.close()
        print("Imported " + str(len(transactions)) + " transactions")

    def update_transaction(self, transaction):
        cursor = self.db.connection.cursor()
        sql = (
            "UPDATE Transaction SET date=%s, amount=%s, pending=%s, merchant_name=%s, description=%s, category=%s, notes=%s, split=%s, parent_transaction_id=%s, hidden_from_budget=%s WHERE id=%s")
        values = (transaction.date,
                  transaction.amount,
                  int(transaction.pending),
                  transaction.merchant_name,
                  transaction.description,
                  transaction.category,
                  transaction.notes,
                  int(transaction.split),
                  transaction.parent_transaction_id,
                  int(transaction.hidden_from_budget),
                  # WHERE id
                  transaction.id)

        cursor.execute(sql, values)
        self.db.connection.commit()
        cursor.close()

    def delete_transaction(self, transaction_id):
        cursor = self.db.connection.cursor()
        cursor.execute("DELETE FROM Transaction WHERE id='" +
                       str(transaction_id) + "';")
        self.db.connection.commit()
        cursor.close()


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
