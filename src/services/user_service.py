from src.repositories.user_repository import UserRepository
from src.models.user_interface import UserCreate
from src.config.providers.firebase_provider import firebase_sign_in

user_repo = UserRepository()

def register_user(user_data: UserCreate) -> str:
    try:
        uid = user_repo.create_user_auth(user_data.email, user_data.password)
        user_repo.save_user_data(uid, {
            "email": user_data.email,
            "name": user_data.name
        })
        return uid
    except Exception as e:
        raise RuntimeError('Failed to register user') from e

def login_user_service(email: str, password: str):
    try:
        return firebase_sign_in(email, password)    
    except Exception as e:
        raise RuntimeError('Failed to login') from e