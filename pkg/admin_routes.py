import random,string,os
import json,requests
from functools import wraps

from flask import render_template,request,abort,redirect,flash,make_response,session,url_for,jsonify
from sqlalchemy.sql import text
from werkzeug.security import generate_password_hash, check_password_hash


from pkg import app,csrf
from pkg.models import db,User,Userupload,Usercomment,Payment,Adminreg
from pkg.forms import *





#This is a decoratoer to help check if there is a user logged in
def login_required(f):
    @wraps(f)
    def login_check(*args,**kwargs):
        if session.get('admin') !=None:
            return f(*args,**kwargs)
        else:
            flash('Access Denied')
            flash('You must be logged in first')
            return redirect('/admin/')
    return login_check


@app.route("/admin/",methods=["POST","GET"])
def admin():
    if request.method =="GET":
        return render_template('admin/adminlog.html')
    else:
        username = request.form.get('username')
        pwd =request.form.get('pwd')
        deets = db.session.query(Adminreg).filter(Adminreg.admin_username==username).first()
        if deets != None:
            hashed_pwd =deets.admin_pwd

            if check_password_hash(hashed_pwd,pwd)==True:
                session['admin']=deets.admin_id

                return redirect(url_for('all_user'))
            else:
                flash('invalid credentials, try again',category='error')
                return redirect('/admin/')
        else:
            flash('invalid Credentials, try again',category='error')
            return redirect('/admin/')


@app.route("/admin/delete/<id>/")
def upload_delete(id):
    upload = db.session.query(Userupload).get_or_404(id)
    filename = upload.upload_filename
    if filename != None and filename !='default.png' and os.path.isfile('pkg/static/uploads/'+filename):
        os.remove('pkg/static/uploads/'+filename)
    db.session.delete(upload)
    db.session.commit()
    flash('project has been deleted',category='projecterror')
    return redirect(url_for('user_project'))



@app.route("/admin/user/<id>/")
def user_delete(id):
    user = db.session.query(User).get_or_404(id)
    filename = user.user_pix
    if filename != None and filename !='default.png' and os.path.isfile('pkg/static/profiles/'+filename):
        os.remove('pkg/static/profiles/'+filename)
    db.session.delete(user)
    db.session.commit()
    flash('user has been deleted Successfully',category='usermsg')
    return redirect(url_for('all_user'))


@app.route("/admin/usercomment/")
def comments():
    id= session.get('admin')
    comments = db.session.query(Usercomment).all()
    userdeets = db.session.query(Adminreg).get_or_404(id)
    return render_template("admin/comments.html",userdeets=userdeets,comments=comments)

@app.route("/admin/comments/<id>/")
def comment_delete(id):
    payment = db.session.query(Usercomment).get_or_404(id)
    db.session.delete(payment)
    db.session.commit()
    flash('User comment has been deleted Successfully',category='commentmsg')
    return redirect(url_for('comments'))



@app.route("/admin/paymentconf/<di>/")
def payment_confirm(di):
    payment = db.session.query(Payment).get_or_404(di)
    payment.payment_status='paid'
    db.session.commit()
    flash('payments has been confirmed',category='paymentmsg')
    return redirect(url_for('transaction'))



@app.route("/admin/payment/<id>/")
def payment_delete(id):
    payment = db.session.query(Payment).get_or_404(id)
    db.session.delete(payment)
    db.session.commit()
    flash('payments has been deleted Successfully',category='paymentmsg')
    return redirect(url_for('transaction'))




@app.route("/adminlogout")
def admin_logout():
    if session.get('admin')!= None:
        session.pop('admin',None)
    return redirect(url_for('admin'))


@app.route("/userproject")
@login_required
def user_project():
    id= session.get('admin')
    updeets = db.session.query(Userupload).all()
    userdeets = db.session.query(Adminreg).get_or_404(id)
    return render_template("admin/user_project.html",userdeets=userdeets,updeets=updeets)


@app.route("/transaction")
@login_required
def transaction():
    id= session.get('admin')
    payments = db.session.query(Payment).all()
    userdeets = db.session.query(Adminreg).get_or_404(id)
    return render_template("admin/transactions.html",userdeets=userdeets,payments=payments)


@app.route("/alluser")
@login_required
def all_user():
    id= session.get('admin')
    deets = db.session.query(User).all()
    userdeets = db.session.query(Adminreg).get_or_404(id)
    return render_template("admin/all_user.html",userdeets=userdeets,deets=deets)