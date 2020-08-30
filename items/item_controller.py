from flask import jsonify,Blueprint,render_template,session,flash
from items import item_dao

item_blueprint=Blueprint('item_blueprint',__name__)

@item_blueprint.route('/categories/<category_id>/items',methods=['GET'])
def get_category_items(category_id):
    if 'user_id' in session:
        session['category_id']=category_id
        get_items=item_dao.get_items(category_id)
        return render_template('item.html',item_list=get_items)
    else:
        flash("please login first", "danger")
        return render_template('login.html')
    # return jsonify(item_dao.get_items(category_id))
