from sqlalchemy import Column, Integer, String,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Item(Base):
    __tablename__ = 'item'

    item_id = Column(Integer, primary_key=True)
    item_name = Column(String)
    item_category = Column(Integer, ForeignKey('category.category_id'))
    seller_name = Column(String)
    item_price = Column(Integer)
    available_quantity = Column(Integer)