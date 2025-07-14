from src.config.connection.firebase_connection import db
from firebase_admin import auth
from typing import Dict, Any

class UserRepository:
    def __init__(self):
        self.collection = db.collection('users')

    def create_user_auth(self, email: str, password: str) -> str:
        try:
            user_record = auth.create_user(email=email, password=password)
            return user_record.uid
        except auth.EmailAlreadyExistsError:
            raise ValueError('This email is already registered.')

    def save_user_data(self, uid: str, data: Dict[str, Any]) -> None:
        try:
            self.collection.document(uid).set(data)  
        except Exception as e:
            raise RuntimeError('Failed to register user') from e