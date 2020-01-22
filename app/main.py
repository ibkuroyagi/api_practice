from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    username: str
    age: int = None
    address: str = None



fake_user_dict = {1:{"id": 1, "username":"user1", "age": "12", "address": "TOKYO"},
                  2:{"id": 2, "username":"user2", "age": "12", "address": "OSAKA"},
                  3:{"id": 3, "username":"user3", "age": "71", "address": "NAGOYA"},
                  4:{"id": 4, "username":"user4", "age": "45", "address": "TOKYO"},
                  5:{"id": 5, "username":"user5", "age": "8", "address": "GIFU"},
                  6:{"id": 6, "username":"user6", "age": "23", "address": "NAGOYA"},
                  }

@app.get("/user/")
async def read_all():
    return fake_user_dict

@app.get("/user/{id}/")
async def read_user(id: int):
    user_result = {"id": id, "username": fake_user_dict[id]["username"]}
    if fake_user_dict[id]["age"]:
        user_result.update({"age": fake_user_dict[id]["age"]})
    if fake_user_dict[id]["address"]:
        user_result.update({"address": fake_user_dict[id]["address"]})
    return user_result


@app.put("/user/{id}/")
async def update_user(id: int, user: User):
    updated_user = user.dict()
    fake_user_dict[id] = updated_user
    return updated_user

@app.post("/user/{id}")
async def add_user(id: int, user: User):
    fake_user_dict[id] = user.dict()
    return fake_user_dict

@app.delete("/user/{id}/")
async def delete_user(id: int):
    del fake_user_dict[id]
    return fake_user_dict

