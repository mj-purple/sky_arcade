import json
from uuid import uuid4

FLIGHT_NUMBER = None

def create_user(name: str, picture: str = None) -> dict:
    with open("users.json", "r+") as write_file:
        data = json.load(write_file)

        user_uuid = str(uuid4())
        data[user_uuid] = {
            "name": name,
            "picture": picture,
            "wins": 0,
            "losses": 0
        }
        json_object = json.dumps(data, indent=4)
        write_file.write(json_object)
        return data

def add_wins(user_uuid: str, wins: int = 1) -> dict:
    with open("users.json", "w") as write_file:
        data = json.load(write_file)[str(FLIGHT_NUMBER)]

        data[user_uuid][wins] += wins
        json.dump(data, write_file)
        return data

def add_losses(user_uuid: str, losses: int = 1) -> dict:
    with open("users.json", "w") as write_file:
        data = json.load(write_file)[str(FLIGHT_NUMBER)]

        data[user_uuid][losses] += losses
        json.dump(data, write_file)
        return data

def get_user_info(user_uuid: str) -> dict:
    with open("users.json", "r") as read_file:
        data = json.load(read_file)[str(FLIGHT_NUMBER)]
        try:
            return data[user_uuid]
        except KeyError:
            return None
        