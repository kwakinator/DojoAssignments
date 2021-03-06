from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re

app = Flask(__name__)
mysql = MySQLConnector(app,'myloginregdb')
bcrypt = Bcrypt(app)
app.secret_key= 'yek_terces'
EMAIL_REGEX= re.compile(r'^[a-zA-Z0-9.+-_]+@[a-zA-Z0-9._-]+\.[a-zA-Z]*$')
PASS_REGEX= re.compile(r'^(?=.*?\d)(?=.*?[A-Z])(?=.*?[a-z])[A-Za-z\d]{8,}$')
NAME_REGEX=re.compile(r'^[a-zA-Z]*$')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=["POST"])
def register():
    user_info={
        'first_name':request.form['first_name'],
        "last_name" :request.form['last_name'],
        "email" :request.form['email'],
        "password" :request.form['password'],
        "conpassword" :request.form['conpassword']
    }
    if len(user_info['first_name'])  < 2 or len(user_info['last_name'])  < 2:
            flash("Must contain at least two characters", 'reg_error')

    if not EMAIL_REGEX.match(user_info['email']):
             flash("Invalid Email Address!", 'reg_error')

    if not NAME_REGEX.match(user_info['first_name']) or not NAME_REGEX.match(user_info['last_name']):
            flash("Letters in your name only!", 'reg_error')

    if not PASS_REGEX.match(user_info['password']):
            flash("Password must be at least 8 characters with one of each: uppercase, lowercase, number", 'reg_error')

    if user_info['conpassword'] != user_info['password']:
            flash("Passwords do not match, please re-enter", "reg_error")

    if "_flashes" in session:
            return redirect('/')

    check_user_query = "SELECT email FROM users WHERE email = :email"
    check_user_data = {
        "email":user_info['email']
    }
    isUser = mysql.query_db(check_user_query, check_user_data)
    if not isUser:
        user_info['password'] = bcrypt.generate_password_hash(user_info['password'])
        newUser_query = "INSERT INTO users(first_name, last_name, email, hashpass, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, now(), now());"
        newUser=mysql.query_db(newUser_query, user_info)
        session['id']=newUser
        userID=session['id']
        return redirect('/success')
    else:
        flash("Error with email please select another email", "reg_error")
        return redirect("/")


@app.route("/login", methods=["POST"])
def login():
    check_query="SELECT id, hashpass FROM users WHERE email=:email"
    check_data={
        "email": request.form['email'],
        "password": request.form['password']
    }
    user_info=mysql.query_db(check_query, check_data)
    if bcrypt.check_password_hash(user_info[0]['hashpass'],check_data['password']):
        return redirect('/success')
    else:
        flash("Password entered is incorrect", "login_error")
        return redirect('/')

@app.route("/success", methods=["GET"])
def success():
    return render_template("success.html")

@app.route("/clear", methods=["POST"])
def clear():
    session.clear()
    return redirect("/")

app.run(debug=True)
