from flask import jsonify,flash,request,Blueprint,render_template,redirect,url_for,session
from carts import cart_dao

cart_blueprint=Blueprint('cart_blueprint',__name__)

@cart_blueprint.route('/cart/<user_id>',methods=['GET'])
def get_cart_items(user_id):
    if 'user_id' in session:
        get_cart=cart_dao.get_cart_details(user_id)
        return render_template('cart.html',carts=get_cart,user_id=user_id)
    else:
        flash("Please login first", "danger")
        return render_template('login.html')
        # return jsonify(cart_dao.get_cart_details(user_id))

@cart_blueprint.route('/cart/<user_id>',methods=['POST'])
def add_to_cart(user_id):
    if 'user_id' in session:
        category_id=session['category_id']
        item_id=request.form.get('item_id')
        quantity=int(request.form.get('quantity'))
        added_cart_obj=cart_dao.insert_to_cart(user_id,item_id,quantity)
        return redirect(url_for('item_blueprint.get_category_items',category_id=category_id))
    else:
        flash("Please login first", "danger")
        return render_template('login.html')
        # return cart_dao.insert_to_cart(user_id,item_id,quantity)

@cart_blueprint.route('/cart/<cart_id>/update',methods=['PATCH'])
def update_cart_item_quantity(cart_id):
    if 'user_id' in session:
        user_id=session['user_id']
        quantity=int(request.form.get('desired_quantity'))
        updated_cart_obj=cart_dao.update_quantity(cart_id,quantity)
        return redirect(url_for('cart_blueprint.get_cart_items',user_id=user_id))
    else:
        flash("Please login first", "danger")
        return render_template('login.html')
        # return cart_dao.update_quantity(cart_id,quantity)

@cart_blueprint.route('/cart/<cart_id>/remove',methods=['DELETE'])
def remove_item_from_cart(cart_id):
    if 'user_id' in session:
        user_id=session['user_id']
        deleted_cart_obj=cart_dao.delete_item(cart_id)
        return redirect(url_for('cart_blueprint.get_cart_items',user_id=user_id))
    else:
        flash("Please login first","danger")
        return render_template('login.html')
        # return cart_dao.delete_item(cart_id)
