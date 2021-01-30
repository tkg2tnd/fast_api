from fastapi import APIRouter

router = APIRouter()

users = {
  "user1": {"name": "user1", "email": "user1@example.com", "age": 20},
  "user2": {"name": "user2", "email": "user2@example.com", "age": 30},
  "user3": {"name": "user3", "email": "user3@example.com", "age": 40},
}

@router.get("/users/", tags=["users"])
async def get_users():
    return {"users": users}

@router.get("/users/me", tags=["users"])
async def get_user_me():
    return {"name": "the current user"}

@router.get("/users/{user_id}", tags=["users"])
async def get_user(user_id: str):
    return {"user": users[user_id]}