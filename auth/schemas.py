from pydantic import BaseModel, EmailStr

#Schema fro new user create
class UserCreate(BaseModel):
    username:str
    email:EmailStr
    password:str
    role:str

#Schema for user login
class UserLogin(BaseModel):
    username:str
    password:str