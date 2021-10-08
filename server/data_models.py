from pydantic import BaseModel

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