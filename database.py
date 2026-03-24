from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import settings




<<<<<<< HEAD
engine = create_engine(settings.DATABASE_URI,connect_args={"check_same_thread": False})
=======
engine = create_engine(settings.DATABASE_URI)
>>>>>>> master
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()





