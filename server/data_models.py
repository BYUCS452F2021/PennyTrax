from pydantic import BaseModel
<<<<<<< HEAD

class Account(BaseModel):
    id: int
    financial_institution_id: str
    user_id: str
    name: str
    type: str
    subtype: str
    available_balance: float
    current_balance: float

class PlaidSignInResult(BaseModel):
    user_id: int
    public_token: str
=======
from typing import Optional


class RegisterRequest(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str
    salt: str


class LoginRequest(BaseModel):
    email: str
    password: str
>>>>>>> feature/add_login
