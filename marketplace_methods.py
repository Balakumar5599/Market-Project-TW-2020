# Methods for api

from marketplace_model import*
db_obj=db_connection()


def login(username,password):
    usernamedata=db_obj.query(User.user_name).filter_by(user_name=username).first()
    passworddata=db_obj.query(User.password).filter_by(password=password).first()

    if username in str(usernamedata) and password in str(passworddata):
        return "You are successfully logged in"
    else:
        return "You are not logged in"
    
    
def get_categories():
    category_dict={}
    categories = db_obj.query(Category).all()
    for category in categories:
        category_dict[category.category_id] = category.category_name
    return [category_dict]


def get_items(category_id):
    item_list=[]
    items=db_obj.query(Item).filter_by(item_category=category_id).all()
    for item in items:
        item_dict={}
        item_dict['item_id']=item.item_id
        item_dict['item_name']=item.item_name
        item_dict['item_price']=item.item_price
        item_dict['seller_name']=item.seller_name
        item_dict['available_quantity']=item.available_quantity
        item_list.append(item_dict)
    return item_list


def get_cart_details(user_id):
    cart_list=[]
    carts=db_obj.query(CustomerCart).filter_by(user_id=user_id).all()
    for cart in carts:
        cart_dict={}
        cart_dict['cart_id']=cart.card_id
        cart_dict['item_id']=cart.item_id
        cart_dict['quantity']=cart.quantity
        cart_dict['total price']=cart.total_price
        cart_dict['buy status']=cart.buy_status
        cart_list.append(cart_dict)
    return cart_list


def insert_to_cart(user_id,item_id,quantity):
    max_quantity=db_obj.query(Item).filter_by(item_id=item_id).one()
    if int(quantity)>max_quantity.available_quantity:
        return "please enter the quantity less than available quantity"
    else:
        item_price=db_obj.query(Item).filter_by(item_id=item_id).one()
        item=CustomerCart(user_id=user_id,item_id=int(item_id),quantity=int(quantity),total_price=int(quantity)*(item_price.item_price),buy_status=False)
        db_obj.add(item)
        db_obj.commit()
        return "Successfully item is post into cart"


def update_quantity(cart_id,quantity):
    cart_item=db_obj.query(CustomerCart).filter_by(card_id=int(cart_id)).first()
    max_quantity=db_obj.query(Item).filter_by(item_id=cart_item.item_id).one()
    if int(quantity)>max_quantity.available_quantity:
        return "please enter the quantity less than available quantity"
    else:
        cart_item.quantity=int(quantity)
        cart_item.total_price=int(quantity)*max_quantity.item_price
        db_obj.add(cart_item)
        db_obj.commit()
        return "successfully updated"


def delete_item(cart_id):
    cart_item=db_obj.query(CustomerCart).filter_by(card_id=int(cart_id)).first()
    db_obj.delete(cart_item)
    db_obj.commit()
    return "successfully removed"
