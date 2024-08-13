from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel              #pydantic for custom type
from sqlmodel import Session
from .db import get_session
from .db import store
from .schema import SignupModel
from .db import delete_user
from .db import get_user
from .schema import UserUpdate
from .db import update_user

app = FastAPI()

# Use the SignupModel as the type for the request body in the endpoint
@app.post("/signup")
def add(data: SignupModel, db:Session = Depends(get_session)):     # custom type  :
    print(f"Data received in API: {data}") 
    student = store(data,db)

    return student

# Perform signup logic here, e.g., store data in database
    
#-------------------------------------------------------------------------------------------------------

@app.delete("/delete-user")
def remove(id : int, db: Session = Depends(get_session)):
    print(f"User id received{id}")
    message = delete_user(id,db)

    return message

#--------------------------------------------------------------------------------------------------------

@app.get("/get-user")
def read(id : int, db: Session = Depends(get_session)):
    print(f"User id received{id}")
    user = get_user(id,db)

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")
    
    return user

#--------------------------------------------------------------------------------------------------------

@app.put("/put-user")
def update(user_input : UserUpdate, db : Session = Depends(get_session)):
    print(f"User input received{user_input}")
    user = update_user(user_input,db)

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User Not found")
    
    return user


    