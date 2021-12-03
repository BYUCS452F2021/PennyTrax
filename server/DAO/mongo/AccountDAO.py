import plaid
from mongo_database import MongoDatabase
from bson.objectid import ObjectId


class AccountDAO:
    def __init__(self):
        self.db = MongoDatabase().db

    def get_institutions_accounts(self, user_id):

        institutions = []
        cash_ins = {
            "financial_institution_name": "Cash Accounts",
            "accounts": []
        }
        # Get Cash Accounts
        cash_accounts = self.db.FinancialAccount.find({"financial_institution_id":None})
        cash_accounts = list(cash_accounts)
        MongoDatabase.clean_id(cash_accounts, ["user"])
        cash_ins["accounts"] += cash_accounts
        institutions.append(cash_ins)

        # Get plaid institutions
        if type(user_id) is str:
            user_id = ObjectId(user_id)
        plaid_institutions = self.db.FinancialInstitution.find({"user_id": user_id}, {"name": True})
        plaid_institutions = list(plaid_institutions)
        MongoDatabase.clean_id(plaid_institutions)

        # # Get plaid accounts and associate with institutions
        fin_ids = [ObjectId(x["id"]) for x in plaid_institutions]
        plaid_accounts = self.db.FinancialAccount.find({"financial_institution_id": {"$in": fin_ids}})
        plaid_accounts = list(plaid_accounts)
        MongoDatabase.clean_id(plaid_accounts, ["financial_institution_id", "user"])

        for ins in plaid_institutions:
            ins['accounts'] = []
            for acc in plaid_accounts:
                if acc['financial_institution_id'] == ins['id']:
                    ins['accounts'].append(acc)

        institutions += plaid_institutions

        return institutions

    def get_institution_access_tokens(self, user_id):
        if type(user_id) is str:
            user_id = ObjectId(user_id)
        ins_tokens = list(self.db.FinancialInstitution.find({"user":user_id}, {"access_token": True}))
        MongoDatabase.clean_id(ins_tokens)
        tokens = [x["token"] for x in ins_tokens]

        return tokens

    def get_account_ids(self, user_id):
        if type(user_id) is str:
            user_id = ObjectId(user_id)
        ins = list(self.db.FinancialAccount.find({"user":user_id}, {"_id": True}))
        MongoDatabase.clean_id(ins)
        acc_ids = [x["id"] for x in ins]

        return acc_ids

    def add_account(self, account):
        result = self.db.FinancialAccount.insert_one(account)
        return str(result.inserted_id)

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
        result = self.db.FinancialInstitution.insert_one({
            "user_id": user_id,
            "name": name,
            "access_token": access_token,
        })
        return str(result.inserted_id)