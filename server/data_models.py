from pydantic import BaseModel
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
