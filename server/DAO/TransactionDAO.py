
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


# TODO: everything.

class TransactionDAO:
    def __init__(self):
        # Init DB connection
        pass

    def get_transactions(self, id=None):
        return dummy_transactions
