from flask import jsonify,request,Blueprint
from user_status import login_dao

login_blueprint=Blueprint('login_blueprint',__name__)

@login_blueprint.route('/login',methods=['POST'])
def user_login():
    username=request.form['user_name']
    password=request.form['password']

    return login_dao.login_status(username,password)