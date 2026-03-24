<<<<<<< HEAD
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from datetime import datetime

from sqlalchemy.orm import relationship

=======
from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime
>>>>>>> master
from database import Base


class Product(Base):
    __tablename__ = 'product'
<<<<<<< HEAD
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String,nullable=False)
    description = Column(String)
    category_id = Column(Integer, ForeignKey('category.id'))
    price = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())

    category = relationship("Category", back_populates="products")  # link to Category



=======
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Integer)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())

>>>>>>> master
