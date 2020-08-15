from sqlalchemy import Column,Integer,String,Boolean,ForeignKey,create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session,sessionmaker
Base=declarative_base()

def db_connection():

    db_url='postgresql://postgres:Balagowtham11@localhost:5432/marketplace'
    sql_db=create_engine(db_url)
    db_session=scoped_session(sessionmaker(bind=sql_db))
    return db_session

db_obj=db_connection()

class User(Base):

    __tablename__='users'

    user_id=Column(Integer,primary_key=True)
    user_name=Column(String,unique=True,nullable=False)
    password=Column(String,nullable=False)
    
    def __init__(self,user_name,password):
        self.user_name=user_name
        self.password=password

    def login_status(self):
        usernamedata = db_obj.query(User.user_name).filter_by(user_name=self.user_name).first()
        passworddata = db_obj.query(User.password).filter_by(password=self.password).first()

        if self.user_name in str(usernamedata) and self.password in str(passworddata):
            return "You are successfully logged in"
        else:
            return "You are not logged in"

class Category(Base):

    __tablename__='category'

    category_id=Column(Integer,primary_key=True)
    category_name=Column(String)
    
    @classmethod
    def get_categories(cls):
        category_dict = {}
        categories = db_obj.query(Category).all()
        for category in categories:
            category_dict[category.category_id] = category.category_name
        return [category_dict]

class Item(Base):

    __tablename__='item'

    item_id=Column(Integer,primary_key=True)
    item_name=Column(String)
    item_category=Column(Integer,ForeignKey('category.category_id'))
    seller_name=Column(String)
    item_price=Column(Integer)
    available_quantity=Column(Integer)
    
    @classmethod
    def get_items(cls,category_id):
        item_list = []
        items = db_obj.query(Item).filter_by(item_category=category_id).all()
        for item in items:
            item_dict = {}
            item_dict['item_id'] = item.item_id
            item_dict['item_name'] = item.item_name
            item_dict['item_price'] = item.item_price
            item_dict['seller_name'] = item.seller_name
            item_dict['available_quantity'] = item.available_quantity
            item_list.append(item_dict)
        return item_list




class CustomerCart(Base):

    __tablename__='customer_cart'

    card_id=Column(Integer,primary_key=True)
    user_id=Column(Integer,ForeignKey('users.user_id'))
    item_id=Column(Integer,ForeignKey('item.item_id'))
    quantity=Column(Integer)
    total_price=Column(Integer)
    buy_status=Column(Boolean)
    
    @classmethod
    def get_cart_details(cls,user_id):
        cart_list = []
        carts = db_obj.query(CustomerCart).filter_by(user_id=user_id).all()
        for cart in carts:
            cart_dict = {}
            cart_dict['cart_id'] = cart.card_id
            cart_dict['item_id'] = cart.item_id
            cart_dict['quantity'] = cart.quantity
            cart_dict['total price'] = cart.total_price
            cart_dict['buy status'] = cart.buy_status
            cart_list.append(cart_dict)
        return cart_list

    @classmethod
    def insert_to_cart(cls,user_id, item_id, quantity):
        max_quantity = db_obj.query(Item).filter_by(item_id=item_id).one()
        if int(quantity) > max_quantity.available_quantity:
            return "please enter the quantity less than available quantity"
        else:
            item_price = db_obj.query(Item).filter_by(item_id=item_id).one()
            item = CustomerCart(user_id=user_id, item_id=int(item_id), quantity=int(quantity),total_price=int(quantity)*(item_price.item_price), buy_status=False)
            db_obj.add(item)
            db_obj.commit()
            return "Successfully item is post into cart"

    @classmethod
    def update_quantity(cls,cart_id, quantity):
        cart_item = db_obj.query(CustomerCart).filter_by(card_id=int(cart_id)).first()
        if cart_item is None:
            return "Cart id is not exist"
        else:
            max_quantity = db_obj.query(Item).filter_by(item_id=cart_item.item_id).one()
            if int(quantity) > max_quantity.available_quantity:
                return "please enter the quantity less than available quantity"
            else:
                cart_item.quantity = int(quantity)
                cart_item.total_price = int(quantity) * max_quantity.item_price
                db_obj.commit()
                return "successfully updated"

    @classmethod
    def delete_item(cls,cart_id):
        cart_item = db_obj.query(CustomerCart).filter_by(card_id=int(cart_id)).first()
        if cart_item is None:
            return "Cart id is not exist"
        else:
            db_obj.delete(cart_item)
            db_obj.commit()
            return "successfully removed"
