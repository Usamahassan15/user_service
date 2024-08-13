from pydantic import BaseModel
from typing  import Optional

# Define your signup model using Pydantic BaseModel
class SignupModel(BaseModel):
    username: str
    email: str
    password: str

# user update input type
class UserUpdate(BaseModel):
    user_id: int
    username : Optional[str] = None
    email: Optional [str] = None
    password: Optional [str] = None
