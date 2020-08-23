from items.item import Item
from database import db_connection

db_obj=db_connection()

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