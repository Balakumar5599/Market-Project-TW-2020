from flask import jsonify,Blueprint,render_template,session,flash
from categories import category_dao

category_blueprint=Blueprint('category_blueprint',__name__)

@category_blueprint.route('/categories',methods=['GET'])
def get_all_categories():
    if 'user_id' in session:
        get_categories=(category_dao.get_categories())
        return render_template('category.html',categories=get_categories)
        #return jsonify(get_categories)
    else:
        flash("please login first","danger")
        return render_template('login.html')
