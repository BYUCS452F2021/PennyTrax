from pydantic import BaseModel
from typing import Optional


class Account(BaseModel):
    id: int
    financial_institution_id: str
    user_id: str
    name: str
    type: str
    subtype: str
    available_balance: float
    current_balance: float


class SimpleAccount(BaseModel):
    name: str
    available_balance: float
    current_balance: float


class Transaction(BaseModel):
    id: str
    account_id: int
    date: str
    amount: float
    pending: bool
    merchant_name: str
    description: str
    category: str
    notes: str
    split: bool
    parent_transaction_id: str
    hidden_from_budget: bool


class TS(BaseModel):
    id: str
    account_id: int


class PlaidSignInResult(BaseModel):
    user_id: int
    public_token: str


class RegisterRequest(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str
    salt: str


class LoginRequest(BaseModel):
    email: str
    password: str
