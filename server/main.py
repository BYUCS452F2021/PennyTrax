from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import DAO.UserDAO as userDAO

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/users/{user_id}")
async def read_user(user_id: int):
    return userDAO.read_user(int(user_id))


class RegisterRequest(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str
    salt: str


@app.post("/register")
async def register(request: RegisterRequest):
    userData = {
        "first_name": request.first_name,
        "last_name": request.last_name,
        "email": request.email,
        "password": request.password,
        "salt": request.salt
    }
    try:
        userDAO.create_user(userData)
    except Exception:
        raise HTTPException(status_code=500, detail="Registration failed")
    else:
        return {"success": True}
