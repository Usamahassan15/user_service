from sqlmodel import SQLModel,Field
from typing import Optional

# model.py is used for Database table creation
class User(SQLModel,table=True):
    id: Optional [int] = Field(primary_key=True,default=None)
    username: str
    email: str
    password: str


