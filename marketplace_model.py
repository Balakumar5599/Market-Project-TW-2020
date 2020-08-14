from sqlalchemy import Column,Integer,String,Boolean,ForeignKey,create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session,sessionmaker
Base=declarative_base()

def db_connection():

    db_url='postgresql://postgres:Balagowtham11@localhost:5432/marketplace'
    sql_db=create_engine(db_url)
    db_session=scoped_session(sessionmaker(bind=sql_db))
    return db_session

class Category(Base):

    __tablename__='category'

    category_id=Column(Integer,primary_key=True)
    category_name=Column(String)

class Item(Base):

    __tablename__='item'

    item_id=Column(Integer,primary_key=True)
    item_name=Column(String)
    item_category=Column(Integer,ForeignKey('category.category_id'))
    seller_name=Column(String)
    item_price=Column(Integer)
    available_quantity=Column(Integer)

class User(Base):

    __tablename__='users'

    user_id=Column(Integer,primary_key=True)
    user_name=Column(String,unique=True,nullable=False)
    password=Column(String,nullable=False)


class CustomerCart(Base):

    __tablename__='customer_cart'

    card_id=Column(Integer,primary_key=True)
    user_id=Column(Integer,ForeignKey('users.user_id'))
    item_id=Column(Integer,ForeignKey('item.item_id'))
    quantity=Column(Integer)
    total_price=Column(Integer)
    buy_status=Column(Boolean)
