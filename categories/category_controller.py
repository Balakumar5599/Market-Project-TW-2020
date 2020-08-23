from flask import jsonify,Blueprint
from categories import category_dao

category_blueprint=Blueprint('category_blueprint',__name__)

@category_blueprint.route('/categories',methods=['GET'])
def get_all_categories():
    return jsonify(category_dao.get_categories())