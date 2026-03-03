

from fastapi import HTTPException
from starlette import status

from app.models.user import User
from app.schemas.user import  UserLogin


def create_user(user, db):

    existing_user = db.query(User).filter_by(username=user.username).first()

    if existing_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="User already exists")

    existing_email = db.query(User).filter_by(email=user.email).first()
    if existing_email:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="email already exists")

    user = User(username=user.username, email=user.email, hash_password=user.password)
    db.add(user)
    db.commit()
    db.refresh(user)
    response= db.query(User).filter_by(username=user.username).first()
    return response


def login_user(user: UserLogin, db):

     user1= db.query(User).filter_by(username=user.username).first()

     if user1 is None:
         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="User not found")

     if user1.email != user.email:
         raise  HTTPException (status_code=status.HTTP_401_UNAUTHORIZED,detail="Incorrect email for user ")

     if user1.hash_password != user.password:
         raise  HTTPException (status_code=status.HTTP_401_UNAUTHORIZED,detail="Incorrect password for user ")


     return  user1
