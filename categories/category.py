from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Category(Base):
    __tablename__ = 'category'

    category_id = Column(Integer, primary_key=True)
    category_name = Column(String)
