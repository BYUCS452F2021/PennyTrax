

dummy_accounts = [
    {
        "financial_institution_name": "Wells Fargo",
        "accounts": [
            {
                "id": 1,
                "financial_institution_id": "abc123",
                "user_id": "demo_user",
                "name": "Credit Card",
                "type": "loan",
                "subtype": "credit_card",
                "available_balance": 1000,
                "current_balance": 1000,
                "mask": 1001
            },
            {
                "id": 2,
                "financial_institution_id": "def123",
                "user_id": "demo_user",
                "name": "Checking",
                "type": "depository",
                "subtype": "checking",
                "available_balance": 800,
                "current_balance": 750,
                "mask": 1002
            },
        ]
    },
    {
        "financial_institution_name": "Chase Bank",
        "accounts": [
            {
                "id": 3,
                "financial_institution_id": "ghi123",
                "user_id": "demo_user",
                "name": "Savings",
                "type": "depository",
                "subtype": "savings",
                "available_balance": "2500",
                "current_balance": "2500",
                "mask": 2001
            },
            {
                "id": 2,
                "financial_institution_id": "def123",
                "user_id": "demo_user",
                "name": "Checking",
                "type": "depository",
                "subtype": "checking",
                "available_balance": 800,
                "current_balance": 750,
                "mask": 2002
            },
        ]
    }
]
    

#TODO: everything.

class AccountDAO:
    def __init__(self):
        # Init DB connection
        pass

    def get_institutions_accounts(self):
        return dummy_accounts

    def get_accounts(self, id=None):
        # Do we still want to support
        # getting a single account by id?
        pass
        # print("ID IS", id)
        # if id is None:
        #     return dummy_accounts
        # else:
        #     return dummy_accounts[0]

    def add_account(self, account):
        return 101