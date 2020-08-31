from database import db_connection
from carts.cart import Cart
from items.item import Item

db_obj=db_connection()

def get_cart_details(user_id):
    
    cart_list=[]
    carts=db_obj.query(Cart).filter_by(user_id=user_id).all()
    items = db_obj.query(Item.item_name).filter_by().all()
    
    for cart in carts:
        cart_dict={}
        cart_dict['cart_id']=cart.cart_id
        cart_dict['item_id']=cart.item_id
        cart_dict['quantity']=cart.quantity
        cart_dict['total price']=cart.total_price
        cart_dict['buy status']=cart.buy_status
        item_name=str(items[(cart.item_id)-1]).replace("('","")
        cart_dict['item_name']=item_name.replace("',)","")
        cart_list.append(cart_dict)
    return cart_list


def insert_to_cart(user_id,item_id,quantity):

    max_quantity = db_obj.query(Item).filter_by(item_id=item_id).one()
    cart_item=db_obj.query(Cart).filter_by(item_id=item_id).first()
    item_price = db_obj.query(Item).filter_by(item_id=item_id).one()

    if int(quantity) > max_quantity.available_quantity:
        return "please enter the quantity less than available quantity"

    elif cart_item is None:
        item = Cart(user_id=user_id, item_id=int(item_id), quantity=int(quantity),total_price=int(quantity)*(item_price.item_price), buy_status=False)
        db_obj.add(item)
        db_obj.commit()
        return "Successfully item is post into cart"
    else:
        cart_item.quantity+=quantity
        cart_item.total_price=(item_price.item_price)*cart_item.quantity
        db_obj.add(cart_item)
        db_obj.commit()
        return "Sucessfully item is post into cart"


def update_quantity(cart_id,quantity):
    cart_item = db_obj.query(Cart).filter_by(cart_id=int(cart_id)).first()
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


def delete_item(cart_id):
    cart_item = db_obj.query(Cart).filter_by(cart_id=int(cart_id)).first()
    if cart_item is None:
        return "Cart id is not exist"
    else:
        db_obj.delete(cart_item)
        db_obj.commit()
        return "successfully removed"
