from fastapi import FastAPI, HTTPException
from DAO.UserDAO import UserDAO
from DAO.AuthTokenDAO import AuthTokenDAO
import data_models

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/users/")
async def get_all_users():
    dao = UserDAO()
    return dao.get_all_users()


@app.get("/users/{user_id}")
async def get_user(user_id: int):
    dao = UserDAO()
    return dao.get_user(int(user_id))


@app.post("/register/")
async def register(request: data_models.RegisterRequest):
    dao = UserDAO()
    try:
        dao.create_user({
            "first_name": request.first_name,
            "last_name": request.last_name,
            "email": request.email,
            "password": request.password,
            "salt": request.salt
        })
    except Exception:
        raise HTTPException(status_code=500, detail="Registration failed")
    else:
        return {"success": True}


@app.post("/login/")
async def login(request: data_models.LoginRequest):
    user_dao = UserDAO()
    auth_token_dao = AuthTokenDAO()
    user = user_dao.get_user_by_email(request.email)
    if user == None:
        return {"success": False, "message": "Username does not exist"}
    elif user["password"] != request.password:
        return {"success": False, "message": "Password is incorrect"}
    else:
        auth_token = auth_token_dao.create_auth_token(user["id"])
        return {"success": True, "auth_token": auth_token}
