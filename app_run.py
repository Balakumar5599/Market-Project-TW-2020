from flask import Flask
from categories.category_controller import *
from items.item_controller import *
from carts.cart_controller import *
from user_status.login_controller import *

app=Flask(__name__)
app.config['DEBUG']=True

app.register_blueprint(category_blueprint)
app.register_blueprint(item_blueprint)
app.register_blueprint(cart_blueprint)
app.register_blueprint(login_blueprint)

if __name__=="__main__":
    app.run()