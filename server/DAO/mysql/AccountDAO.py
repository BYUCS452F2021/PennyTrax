from mysql_database import MysqlDatabase

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
        self.db = MysqlDatabase()

    def get_institutions_accounts(self, user_id):
        institutions = []

        # Get Cash Accounts
        cursor = self.db.connection.cursor(dictionary=True)
        cursor.execute(
            "SELECT * FROM FinancialAccount WHERE financial_institution_id IS NULL AND user_id=" + str(user_id) + ";")
        accounts = cursor.fetchall()

        if len(accounts) > 0:
            cash_accounts = {
                "financial_institution_name": "Cash Accounts",
                "accounts": []
            }
            for account in accounts:
                cash_accounts["accounts"].append(account)
            institutions.append(cash_accounts)

        # Get plaid institutions
        cursor.execute(
            "SELECT name as financial_institution_name, id FROM FinancialInstitution WHERE user_id=" + str(user_id) + ";")
        institution_results = cursor.fetchall()

        if len(institution_results) == 0:
            return institutions

        # Get accounts for each institution
        formatted_ids = ",".join([str(x['id']) for x in institution_results])
        cursor.execute(
            "SELECT * FROM FinancialAccount WHERE financial_institution_id IN (" + formatted_ids + ") ;")
        accounts = cursor.fetchall()

        # This is O(nm) which is too slow. TODO: find a more efficient way to do this
        for ins in institution_results:
            ins['accounts'] = []
            for acc in accounts:
                if acc['financial_institution_id'] == ins['id']:
                    ins['accounts'].append(acc)

        institution_results.extend(institutions)

        return institution_results

    def get_institution_access_tokens(self, user_id):
        cursor = self.db.connection.cursor(dictionary=True)
        cursor.execute(
            "SELECT access_token FROM FinancialInstitution WHERE user_id=" + str(user_id) + ";")
        results = cursor.fetchall()

        tokens = []
        for token in results:
            tokens.append(token["access_token"])

        return tokens

    def get_account_ids(self, user_id):
        cursor = self.db.connection.cursor(dictionary=True)
        cursor.execute(
            "SELECT id FROM FinancialAccount WHERE user_id=" + str(user_id) + ";")
        results = cursor.fetchall()

        accounts = []
        for account in results:
            accounts.append(account["id"])

        return accounts

    def add_account(self, account):
        cursor = self.db.connection.cursor()
        sql = (
            "INSERT INTO FinancialAccount (id, financial_institution_id, user_id, name, type, subtype, mask, available_balance, current_balance) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
        values = (account["id"],
                  account["financial_institution_id"],
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

    def update_accounts(self, accounts):
        cursor = self.db.connection.cursor()
        sql = (
            "UPDATE FinancialAccount SET available_balance=%s, current_balance=%s WHERE id=%s")
        for account in accounts:
            values = (account["available_balance"],
                      account["current_balance"],
                      account["id"])
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
