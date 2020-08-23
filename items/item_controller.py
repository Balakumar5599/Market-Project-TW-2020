from flask import jsonify,Blueprint
from items import item_dao

item_blueprint=Blueprint('item_blueprint',__name__)

@item_blueprint.route('/categories/<category_id>/items',methods=['GET'])
def get_category_items(category_id):
    return jsonify(item_dao.get_items(category_id))
