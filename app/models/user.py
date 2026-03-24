from sqlalchemy import Column, Integer, String,DateTime
from datetime import datetime
from database import  Base


class User(Base):
    __tablename__ = 'user'
<<<<<<< HEAD
    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String ,  nullable=False)
    email = Column(String, nullable=False)
=======
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
>>>>>>> master
    hash_password = Column(String)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
