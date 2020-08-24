from user_status.user import User
from database import db_connection

db_obj=db_connection()

def login_status(username,password):
    user=db_obj.query(User).filter_by(user_name=username,password=password).first()
    if user != None:
        return "You are successfully logged it"
    else:
        return "You are not logged in"