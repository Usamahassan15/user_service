from sqlmodel import create_engine, SQLModel,Session,select
from .schema import SignupModel
from .model import User
from .schema import UserUpdate
from .config import settings

# Create connection of your app with DB using create engine pkg
engine = create_engine(settings.database_url)

# Get Session
def get_session():
    SQLModel.metadata.create_all(engine)    # create all table defined in model.py 
    with Session(engine) as session:        # create session to send trasation in DB Table
        yield session

#--------------------------------------------------------------------------------------------------

# store in db
def store(data: SignupModel, db: Session):
    new_student = User(
        username= data.username,
        email= data.email,
        password= data.password
    )

    db.add(new_student)    # save data in the session
    db.commit()           # save data in DB table 
    db.refresh(new_student)     # refresh new student with updated data in db 

    return new_student
    
# -------------------------------------------------------------------------------------------------

# Delete user
def delete_user(id : int, db: Session):
    statement = select(User).where(User.id==id)
    user_info = db.exec(statement).first()
    db.delete(user_info)

    db.commit()
    return f"User with this {id} deleted successfully"

#--------------------------------------------------------------------------------------------------

# Get user info
def get_user(id : int, db : Session): 
    statement = select(User).where(User.id==id)
    user_info = db.exec(statement).first()

    return user_info

#--------------------------------------------------------------------------------------------------

# Update user info
def update_user(user_input : UserUpdate, db : Session):
    statement = select(User).where(User.id==user_input.user_id)
    user_info = db.exec(statement).first()

    if not user_info:
        return None
    
    if user_input.username is not None:
        user_info.username = user_input.username

    if user_input.email is not None:
        user_info.email = user_input.email

    if user_input.password is not None:
        user_info.password = user_input.password

    db.add(user_info)
    db.commit()     # commit means save data in db
    db.refresh(user_info)

    return user_info
