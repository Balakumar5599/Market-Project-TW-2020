from categories.category import Category
from database import db_connection

db_obj=db_connection()

def get_categories():
    category_dict={}
    categories = db_obj.query(Category).all()
    for category in categories:
        category_dict[category.category_id]=category.category_name
    return category_dict
