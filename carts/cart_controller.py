from flask import jsonify,request,Blueprint
from carts import cart_dao

cart_blueprint=Blueprint('cart_blueprint',__name__)

@cart_blueprint.route('/cart/<user_id>',methods=['GET'])
def get_cart_items(user_id):
    return jsonify(cart_dao.get_cart_details(user_id))

@cart_blueprint.route('/cart/<user_id>',methods=['POST'])
def add_to_cart(user_id):
    item_id=request.form['item_id']
    quantity=request.form['quantity']
    return cart_dao.insert_to_cart(user_id,item_id,quantity)

@cart_blueprint.route('/cart/<cart_id>',methods=['PATCH'])
def update_cart_item_quantity(cart_id):
    quantity=request.form['quantity']
    return cart_dao.update_quantity(cart_id,quantity)

@cart_blueprint.route('/cart/<cart_id>',methods=['DELETE'])
def remove_item_from_cart(cart_id):
    return cart_dao.delete_item(cart_id)