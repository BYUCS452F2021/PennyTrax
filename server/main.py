from fastapi import FastAPI, HTTPException
from DAO.UserDAO import UserDAO
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


@app.post("/register")
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
