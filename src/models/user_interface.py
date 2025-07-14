from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    name: str
    
class LoginData(BaseModel):
    email: str
    password: str
    
class UserToken(BaseModel):
    idToken: str
    refreshToken: str
    uid: str
