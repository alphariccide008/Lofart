from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()




class User(db.Model):
    user_id = db.Column(db.Integer(),primary_key=True,autoincrement=True)
    user_fname =db.Column(db.String(64),index=True,nullable=False)
    user_lname =db.Column(db.String(64),index=True,nullable=False)
    user_add =db.Column(db.String(200),index=True,nullable=False)
    user_city =db.Column(db.String(64),index=True,nullable=False)
    user_reg =db.Column(db.DateTime(),default=datetime.utcnow )
    user_email =db.Column(db.String(100),index=True,nullable=False)
    user_phone =db.Column(db.String(50),index=True,nullable=False)
    user_profile =db.Column(db.String(300),index=True)
    user_pix=db.Column(db.String(120),nullable=True) 
    user_username =db.Column(db.String(100),index=True,nullable=False)
    user_state =db.Column(db.String(100),index=True,nullable=True)
    user_lga =db.Column(db.String(100),index=True,nullable=True)
    user_password =db.Column(db.String(225),index=True,nullable=False)
    user_usertype =db.Column(db.String(100),index=True,nullable=False)
    userpayment = db.relationship("Payment", backref="paymentdeets",cascade='all,delete-orphan')
    uploadby = db.relationship("Userupload", backref="userupload",cascade='all,delete-orphan')
    commentby = db.relationship("Usercomment", backref="usercommentby",cascade='all,delete-orphan')
    orderby = db.relationship("Order", back_populates="userordering",cascade='all,delete-orphan')






class Payment(db.Model):
    payment_id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    payment_status = db.Column(db.String(10), index=True, nullable=False)
    payment_amt = db.Column(db.Integer(), index=True, nullable=False)
    refno = db.Column(db.String(12), index=True, nullable=False)
    payment_date = db.Column(db.DateTime(), default=datetime.utcnow)
    payment_user_id = db.Column(db.Integer(), db.ForeignKey('user.user_id', ondelete='CASCADE', onupdate='CASCADE'))
    payment_order_id = db.Column(db.Integer(), db.ForeignKey('order.order_id', ondelete='CASCADE', onupdate='CASCADE'))
    paymentupd = db.relationship("Userupload", backref='payment')  # assuming 'uploaddeets' is a backref attribute
    ptupload = db.Column(db.Integer(), db.ForeignKey('userupload.upload_id'))





class Userupload(db.Model):
    upload_id = db.Column(db.Integer(),primary_key=True,autoincrement=True)
    upload_filename =db.Column(db.String(200),index=True,nullable=False)
    upload_desc =db.Column(db.String(500),index=True,nullable=False)
    upload_amt =db.Column(db.Integer(),index=True,nullable=False)
    upload_date = db.Column(db.DateTime(), default=datetime.utcnow)  
    upload_user_id=db.Column(db.Integer(), db.ForeignKey('user.user_id',ondelete='CASCADE', onupdate='CASCADE'))

    





class Usercomment(db.Model):
    usercomment_id = db.Column(db.Integer(),primary_key=True,autoincrement=True)
    user_comment=db.Column(db.String(300),index=True,nullable=True)
    comment_date = db.Column(db.DateTime(), default=datetime.utcnow)  
    comment_user_id=db.Column(db.Integer(), db.ForeignKey('user.user_id'))
    comment_upload_id=db.Column(db.Integer(), db.ForeignKey('userupload.upload_id',ondelete='CASCADE', onupdate='CASCADE'))
    commentup = db.relationship("Userupload", backref="usercomment")


 


class Order(db.Model):
    order_id = db.Column(db.Integer(),primary_key=True,autoincrement=True)
    order_amt=db.Column(db.Integer(),index=True,nullable=False)
    order_date = db.Column(db.DateTime(), default=datetime.utcnow)  
    order_user_id=db.Column(db.Integer(), db.ForeignKey('user.user_id',ondelete='CASCADE', onupdate='CASCADE'))
    userordering = db.relationship("User", back_populates="orderby")

    




class Adminreg(db.Model):
    admin_id=db.Column(db.Integer, autoincrement=True,primary_key=True)
    admin_username=db.Column(db.String(20),nullable=False)
    admin_pwd=db.Column(db.String(200),nullable=False)

    
