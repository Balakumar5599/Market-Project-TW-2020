from flask import jsonify,request,Blueprint,session,render_template,redirect,url_for,flash
from user_status import login_dao

login_blueprint=Blueprint('login_blueprint',__name__)
home_blueprint=Blueprint('home_blueprint',__name__)


@login_blueprint.route('/login',methods=['GET','POST'])
def user_login():
    if request.method=='POST':
        username=request.form.get('username')
        password=request.form.get('password')
        (status,user)=login_dao.login_status(username,password)
        if status==True:
            session['user_id']=user.user_id
            session['username']=username
            return redirect(url_for('home_blueprint.home'))
        else:
            flash("Invalid username or password","danger")
            return render_template('login.html')
    return render_template('login.html')


@home_blueprint.route('/home',methods=['GET'])
def home():
    if 'user_id' in session:
        user_id=session['user_id']
        return render_template('home.html')
    else:
        flash("please login first","danger")
        return redirect(url_for('login_blueprint.user_login'))
