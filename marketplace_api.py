from flask import request,jsonify,url_for,redirect,Flask
from marketplace_model import*

app=Flask(__name__)
app.config['DEBUG']=True

@app.route('/login',methods=['POST'])
def user_login():
    username=request.form['user_name']
    password=request.form['password']
    return login_status(username,password)

@app.route('/categories',methods=['GET'])
def get_category():
    return jsonify(get_categories())

@app.route('/categories/<category_id>/items',methods=['GET'])
def get_category_item(category_id):
    return jsonify(get_items(category_id))

@app.route('/cart/<user_id>',methods=['GET'])
def get_cart_item(user_id):
    return jsonify(get_cart_details(user_id))

@app.route('/cart/<user_id>',methods=['POST'])
def add_to_cart(user_id):
    item_id=request.form['item_id']
    quantity=request.form['quantity']
    return insert_to_cart(user_id,item_id,quantity)

@app.route('/cart/<cart_id>',methods=['PATCH'])
def update_cart_item_quantity(cart_id):
    quantity=request.form['quantity']
    return update_quantity(cart_id,quantity)

@app.route('/cart/<cart_id>',methods=['DELETE'])
def remove_item_from_cart(cart_id):
    return delete_item(cart_id)

app.run()
