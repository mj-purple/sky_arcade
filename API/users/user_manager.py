import json
from fastapi import HTTPException
from uuid import uuid4

FLIGHT_NUMBER = None
user_json = "users/users.json"

async def create_user(name: str, picture: str = None) -> dict:
    with open(user_json, "r") as read_file:
        data = json.load(read_file)

    user_uuid = str(uuid4())
    data[user_uuid] = {"name": name, "picture": picture, "points": 0}
    with open(user_json, "w") as write_file:
        json.dump(data, write_file, indent=2)

    return {user_uuid: data[user_uuid]}

async def delete_user(user_uuid: str) -> dict:
    with open(user_json, "r") as read_file:
        data = json.load(read_file)

    user = data.get(user_uuid)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    del data[user_uuid]

    with open(user_json, "w") as write_file:
        json.dump(data, write_file, indent=2)
    return {"ok": True}

async def add_points(user_uuid: str, points: int = 1) -> dict:
    with open(user_json, "r") as read_file:
        data = json.load(read_file)
    user = data.get(user_uuid)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    data[user_uuid]["points"] += points
    with open(user_json, "w") as write_file:
        json.dump(data, write_file, indent=2)
    return {user_uuid: data[user_uuid]}

async def remove_points(user_uuid: str, points: int = 1) -> dict:
    with open(user_json, "r") as read_file:
        data = json.load(read_file)
    user = data.get(user_uuid)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    data[user_uuid]["points"] -= points
    with open(user_json, "w") as write_file:
        json.dump(data, write_file, indent=2)
    return {user_uuid: data[user_uuid]}

async def get_user(user_uuid: str) -> dict:
    with open(user_json, "r") as read_file:
        data = json.load(read_file)
    
    user = data.get(user_uuid)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

async def get_all_users() -> dict:
    with open(user_json, "r") as read_file:
        data = json.load(read_file)
    if data == {}:
        raise HTTPException(status_code=404, detail="No users found")
    return data
