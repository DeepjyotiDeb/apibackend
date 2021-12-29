from typing import List, Optional
from pydantic import BaseModel
from uuid import UUID
import datetime

uid = UUID

class Blogger(BaseModel): 
    title: str
    summary: str
    body: str
    created_on: Optional[datetime.datetime]
    id: Optional[int]
    class Config():
        orm_mode = True

class Update_Post(BaseModel):
    title: Optional[str] = None
    summary: Optional[str] = None
    body: Optional[str] = None

class User(BaseModel):
    name: str
    email: str
    password: str

class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[Blogger] = []
    class Config():
        orm_mode = True

class ShowBlog(BaseModel):
    title: str
    summary: str
    body: str
    creator: ShowUser
    class Config():
        orm_mode =True

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None