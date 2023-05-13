import json
from fastapi import HTTPException
from uuid import uuid4

FLIGHT_NUMBER = None
user_json = "users.json"

async def create_user(name: str, picture: str = None) -> dict:
    with open(user_json, "r") as read_file:
        data = json.load(read_file)

    user_uuid = str(uuid4())
    data[user_uuid] = {"name": name, "picture": picture, "wins": 0, "losses": 0}
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


async def add_wins(user_uuid: str, wins: int = 1) -> dict:
    with open(user_json, "r") as read_file:
        data = json.load(read_file)
    user = data.get(user_uuid)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    data[user_uuid]["wins"] += wins
    with open(user_json, "w") as write_file:
        json.dump(data, write_file, indent=2)
    return {user_uuid: data[user_uuid]}

async def add_losses(user_uuid: str, losses: int = 1) -> dict:
    with open(user_json, "r") as read_file:
        data = json.load(read_file)
    user = data.get(user_uuid)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    data[user_uuid]["losses"] += losses
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
    return data
        
