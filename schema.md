# PennyTrax Database Schema

## Tables

*Primary Keys are <u>underlined</u>
*Foreign Keys are **bolded**

#### User
This represents a user of the application that can register, sign-in, and view their financial data.

- <u>id</u>
- first_name
- last_name
- email: A users email used as their username
- password: This is the hashed value of the users input password and their salt
- salt: This is a randomly generated string used to hash a users input password


#### FinancialInstitution
This represents a financial institution supported by plaid that a user can connect to.
- <u>id</u>
- **user_id**: References a User
- name: This is the name of the financial institution
- access_token: This is the access_token used to access a users financial institution via the plaid api

#### FinancialAccount
This represents one account that the user can add to their account. This relates to the financial institution because a user may have several accounts from a single institution. It also relates to Transactions because each transaction comes from one of the user’s accounts. 
- <u>id</u>: (External key: account_id)
- **financial_institution_id**: References a FinancialInstitution
- **user_id**: References a User
- name: Name of the bank/institution
- type: Ex: Depository
- subtype: Ex: Credit/Debit/Cash
- available_balance: The amount of money that is not pending
- current_balance: The total amount in the account, including pending transactions

#### Transaction
Financial transactions performed by users, either pulled from the financial data API or created manually.
- <u>id</u>: (External key: transaction_id)
- **account_id**: References a FinancialAccount
- date: Date the transaction occurred
- amount: The is the amount for the transaction in cents
- pending: (bool)
- merchant_name: (External key from API: merchant_name) the name of the merchant who initiated the transaction.
- description: (External key from API: name)
- category: (External key from API: category): the category of the transaction. The user will be able to modify this value.
- notes: (user-defined notes; defaults to NULL)
- split: (bool) This indicates whether or not a transaction was split into multiple categories
- parent_transaction_id: (Recursive foreign key; can be NULL) Another transaction from which the current transaction was split
- hidden_from_budget: Indicates whether or not to include amount in budget limit and spending chart by category

#### Budget
This represents a budget that a user creates, listing several categories of purchases and the target amounts spent for each category. It relates to the user table because each budget is associated with one user.
- <u>id</u>
- **user_id**: References a User
- category: The category that a user wants to limit their monthly spending in
- target_amount: Limit of money user wants to spend each month in the specified category in cents

