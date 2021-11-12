

from database import Database
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


class AccountDAO:
    def __init__(self):
        self.db = Database()

    def get_institutions_accounts(self, user_id):
        cursor = self.db.connection.cursor(dictionary=True)
        cursor.execute(
            "SELECT name as financial_institution_name, id FROM FinancialInstitution WHERE user_id=" + str(user_id) + ";")
        institutions = cursor.fetchall()

        formatted_ids = ",".join([str(x['id']) for x in institutions])
        cursor.execute(
            "SELECT * FROM FinancialAccount WHERE financial_institution_id IN (" + formatted_ids + ") ;")
        accounts = cursor.fetchall()

        # This is O(nm) which is too slow. TODO: find a more efficient way to do this
        for ins in institutions:
            ins['accounts'] = []
            for acc in accounts:
                if acc['financial_institution_id'] == ins['id']:
                    ins['accounts'].append(acc)

        return institutions

    def add_account(self, account):
        cursor = self.db.connection.cursor()
        sql = (
            "INSERT INTO User (financial_institution_id, user_id, name, type, subtype, mask, available_balance, current_balance) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
        values = (account["financial_institution_id"],
                  account["user_id"],
                  account["name"],
                  account["type"],
                  account["subtype"],
                  account["mask"],
                  account["available_balance"],
                  account["current_balance"],)
        cursor.execute(sql, values)
        id = cursor.lastrowid
        self.db.connection.commit()
        cursor.close()
        return id

    def add_institution_accounts(self, user_id, financial_institution_id, accounts):
        cursor = self.db.connection.cursor()
        sql = (
            "INSERT INTO FinancialAccount (id, financial_institution_id, user_id, name, type, subtype, mask) VALUES (%s, %s, %s, %s, %s, %s, %s)")
        for account in accounts:
            values = (account["id"],
                      financial_institution_id,
                      user_id,
                      account["name"],
                      account["type"],
                      account["subtype"],
                      account["mask"])
            cursor.execute(sql, values)
        self.db.connection.commit()
        cursor.close()

    def add_institution(self, user_id, name, access_token):
        cursor = self.db.connection.cursor()
        sql = (
            "INSERT INTO FinancialInstitution (user_id, name, access_token) VALUES (%s, %s, %s)")
        values = (user_id, name, access_token)
        cursor.execute(sql, values)
        id = cursor.lastrowid
        self.db.connection.commit()
        cursor.close()
        return id
