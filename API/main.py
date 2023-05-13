from fastapi import FastAPI
import users.user_manager as user_manager

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

@app.patch("/user/add-points", tags=["Users"])
async def add_points(user_uuid: str, points: int = 1):
    return await user_manager.add_points(user_uuid, points)

@app.patch("/user/remove-points", tags=["Users"])
async def remove_points(user_uuid: str, points: int = 1):
    return await user_manager.remove_points(user_uuid, points)

@app.delete("/user/delete/{user_uuid}", tags=["Users"])
async def delete_user(user_uuid: str):
    return await user_manager.delete_user(user_uuid)

@app.delete("/users/clear", tags=["Users"])
async def clear_users():
    return await user_manager.clear_users()