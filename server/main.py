from fastapi import FastAPI
import DAO.UserDAO as userDAO

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/user/{user_id}")
async def read_user(user_id):
    return userDAO.read_user(int(user_id))
