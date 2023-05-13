from fastapi import FastAPI
import API.users.user_manager as user_manager

app = FastAPI()


#USERS
@app.get("/users", tags=["Users"])
async def get_all_users():
    return await user_manager.get_all_users()

@app.get("/user/{user_uuid}", tags=["Users"])
async def get_user(user_uuid: str):
    return await user_manager.get_user(user_uuid)

@app.post("/user/create", tags=["Users"])
async def create_user(name: str, picture: str = None):
    return await user_manager.create_user(name, picture)

@app.patch("/user/add-wins", tags=["Users"])
async def add_wins(user_uuid: str, wins: int = 1):
    return await user_manager.add_wins(user_uuid, wins)

@app.patch("/user/add-losses", tags=["Users"])
async def add_losses(user_uuid: str, losses: int = 1):
    return await user_manager.add_losses(user_uuid, losses)

@app.delete("/user/delete", tags=["Users"])
async def delete_user(user_uuid: str):
    return await user_manager.delete_user(user_uuid)
