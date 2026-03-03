from fastapi import APIRouter
from fastapi.params import Depends

from app.api.deps import get_db
from app.schemas.user import UserRegister, UserResponse, UserLogin
from app.curd.user import create_user,login_user

router = APIRouter(prefix="/auth")


@router.post("/register",response_model=UserResponse)
def register_user(user: UserRegister, db=Depends(get_db)):
    """ Run user registration route """
    user= create_user(user, db)
    return  user


@router.post("/login",response_model=UserResponse)
def login(user: UserLogin, db=Depends(get_db)):
     """ Run user login route """
     user1= login_user(user,db)

     return user1
