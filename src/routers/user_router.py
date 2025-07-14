from fastapi import APIRouter
from src.models.user_interface import LoginData, UserCreate, UserToken
from src.controllers.user_controller import create_user_controller, login_user_controller

user_router = APIRouter()

@user_router.post('/signup', tags=["Usuários"])
async def signup(user: UserCreate):
    return create_user_controller(user)

@user_router.post("/login", response_model=UserToken, tags=["Usuários"])
async def login_user(user: LoginData):
    return login_user_controller(user)