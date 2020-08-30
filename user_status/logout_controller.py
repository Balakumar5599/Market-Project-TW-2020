from flask import session,Blueprint,redirect,url_for

logout_blueprint=Blueprint('logout_blueprint',__name__)

@logout_blueprint.route('/logout',methods=['GET'])
def user_logout():
    session.pop('user_id',None)
    session.pop('username',None)
    print("you are logged out")
    return redirect(url_for('login_blueprint.user_login'))
