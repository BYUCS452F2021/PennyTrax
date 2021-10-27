

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
from database import Database

class AccountDAO:
    def __init__(self):
        self.db = Database()

    def get_institutions_accounts(self, user_id):
        cursor = self.db.connection.cursor(dictionary=True)
        cursor.execute("SELECT name as financial_institution_name, id FROM FinancialInstitution WHERE user_id=" + str(user_id) + ";")
        institutions = cursor.fetchall()

        formatted_ids = ",".join([str(x['id']) for x in institutions])
        cursor.execute("SELECT * FROM FinancialAccount WHERE financial_institution_id IN (" + formatted_ids + ") ;")
        accounts = cursor.fetchall()

        # This is O(nm) which is too slow. TODO: find a more efficient way to do this
        for ins in institutions:
            ins['accounts'] = []
            for acc in accounts:
                if acc['financial_institution_id'] == ins['id']:
                    ins['accounts'].append(acc)

        return institutions

    def add_account(self, account):
        return 101