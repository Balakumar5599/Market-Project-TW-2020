from sqlalchemy import Column, Integer, String,ForeignKey,Boolean
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Cart(Base):
    __tablename__ = 'cart'

    cart_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    item_id = Column(Integer, ForeignKey('item.item_id'))
    quantity = Column(Integer)
    total_price = Column(Integer)
    buy_status = Column(Boolean)