
dummy_accounts = [
    {
        "id": 1,
        "financial_institution_id": "abc123",
        "user_id": "demo_user",
        "name": "Credit Card",
        "type": "loan",
        "subtype": "credit_card",
        "available_balance": "1000",
        "current_balance": "1000"
    },
    {
        "id": 2,
        "financial_institution_id": "def123",
        "user_id": "demo_user",
        "name": "Checking",
        "type": "depository",
        "subtype": "checking",
        "available_balance": "800",
        "current_balance": "750"
    },
    {
        "id": 3,
        "financial_institution_id": "ghi123",
        "user_id": "demo_user",
        "name": "Savings",
        "type": "depository",
        "subtype": "savings",
        "available_balance": "2500",
        "current_balance": "2500"
    }
]

#TODO: everything.

class AccountDAO:
    def __init__(self):
        # Init DB connection
        pass

    def get_accounts(self, id=None):
        print("ID IS", id)
        if id is None:
            return dummy_accounts
        else:
            return dummy_accounts[0]

    def add_account(self, account):
        return 101