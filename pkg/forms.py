from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileRequired,FileAllowed
from wtforms import StringField, SubmitField, TextAreaField ,PasswordField,RadioField
from wtforms.validators import Email, DataRequired, EqualTo, Length



class RegForm(FlaskForm):
    fname = StringField("FirstName",validators=[DataRequired(message="Input your First Name")])
    lname = StringField("Last Name",validators=[DataRequired(message="Input your Last Name")])
    usermail = StringField("Email",validators=[Email(),DataRequired(message="Input valid email")])
    pwd = PasswordField("Enter Password",validators=[DataRequired(message="Password must match")])
    
    confpwd = PasswordField("Confirm Password",validators=[DataRequired(message="password don't match"),EqualTo("pwd")])
    profile = TextAreaField("Your Profile")
    btnsubmit = SubmitField("Register")


class NewForm(FlaskForm):
    fname = StringField("FirstName",validators=[DataRequired(message="Input your First Name")])
    lname = StringField("Last Name",validators=[DataRequired(message="Input your Last Name")])
    email = StringField("Email",validators=[Email(),DataRequired(message="Input valid email")])
    address = StringField("Address",validators=[DataRequired(message="Input valid email")])
    phone = StringField("Phone number",validators=[DataRequired(message="Input valid email")])
    city = StringField("City",validators=[DataRequired(message="Input valid email")])
    status= RadioField("usertype",validators=[DataRequired(message="Input valid email")])
    uname = StringField("Username",validators=[DataRequired(message="Input your First Name")])
    state = StringField("state",validators=[Email(),DataRequired(message="Input state")])
    lga = StringField("Lga",validators=[Email(),DataRequired(message="Input local Government")])
    pwd = PasswordField("Enter Password",validators=[DataRequired(message="Password must match")])
    confpwd = PasswordField("Confirm Password",validators=[DataRequired(message="password don't match"),EqualTo("pwd")])
    profile = TextAreaField("Your Profile")
    btnsubmit = SubmitField("Register")

class ProfileForm(FlaskForm):
    fullname = StringField("First Name",validators=[DataRequired(message="Input your First Name")])
    lastname = StringField("Last Name",validators=[DataRequired(message="Input your First Name")])
    phone = StringField("Phone ",validators=[DataRequired(message="Input your First Name")])
    city = StringField("City",validators=[DataRequired(message="Input your First Name")])
    status = RadioField("Profession ",validators=[DataRequired(message="Input your First Name")])
    address = StringField("Address ",validators=[DataRequired(message="Input your First Name")])
    profile = TextAreaField("Biodata ",validators=[DataRequired(message="Input your First Name")])
    dp = FileField("upload a Profile picture",validators=[FileAllowed(['jpg','png','jpeg'])])
    state = StringField("state ",validators=[DataRequired(message="Input your First Name")])
    lga = StringField("local governmeent ",validators=[DataRequired(message="Input your First Name")])



    dp = FileField("upload a Profile picture",validators=[FileRequired(),FileAllowed(['jpg','png','jpeg'])])
    btnsubmit = SubmitField("Update Profile")


class Uploadfile(FlaskForm):
        projectdp = FileField("upload Project Image",validators=[FileAllowed(['jpg','png','jpeg'])])
        projectdescription = TextAreaField("Description",validators=[DataRequired(message="Please Input A description")])
        projectprice= StringField("Project Price",validators=[DataRequired(message="Price")])
        btnsubmit = SubmitField("Upload Project")

class ChangePass(FlaskForm):
    email= StringField("Input Email",validators=[DataRequired(message="Enter email")])
    pwd = PasswordField("Enter Old Password",validators=[DataRequired(message="incorrect Password")])
    newpwd = PasswordField("Confirm Password",validators=[DataRequired(message="Fill the field")])
    btnsubmit = SubmitField("Update Profile")

class payForm(FlaskForm):
    fullname= StringField("FirstName",validators=[DataRequired(message="input your fullname")])   
    email= StringField("Email",validators=[Email(message="Invalid Email"),DataRequired(message='Email must be suplied')])
    amt= StringField("Amt",validators=[Email(message="Invalid Email"),DataRequired(message='Email must be suplied')])
    btnsubmit=SubmitField("continue")


    