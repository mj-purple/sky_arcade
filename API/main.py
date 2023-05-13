from fastapi import FastAPI
import user_manager

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "API_UP"}

@app.post("/create/user")
async def create_user(name: str, picture: str = None):
    return user_manager.create_user(name, picture)