from src.services.user_service import login_user_service, register_user
from src.models.user_interface import LoginData, UserCreate
from fastapi import HTTPException

def create_user_controller(user_data: UserCreate):
    try:
        uid = register_user(user_data)
        return {"message": "User created successfully!", "uid": uid}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

def login_user_controller(user_data: LoginData):
    try:
        token_data = login_user_service(user_data.email, user_data.password)
        return token_data
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))