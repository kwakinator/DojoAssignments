from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re

app = Flask(__name__)
mysql = MySQLConnector(app,'walldb')
bcrypt = Bcrypt(app)
app.secret_key= 'yek_terces'
EMAIL_REGEX= re.compile(r'^[a-zA-Z0-9.+-_]+@[a-zA-Z0-9._-]+\.[a-zA-Z]*$')
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

    if len(user_info['password']) < 8:
            flash("Password must be at least 8 characters", 'reg_error')

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
        session['user']= {
            "id": newUser
        }
        user_id = session['user']['id']
        return redirect('/wall')
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
    if user_info and bcrypt.check_password_hash(user_info[0]['hashpass'],check_data['password']):
        session['user']={
            "id": user_info[0]['id']
        }
        user_id=session['user']['id']
        return redirect('/wall')
    else:
        flash("Incorrect Password or Email", "login_error")
        return redirect('/')

@app.route("/wall", methods=["GET"])
def wall():
    user_id=session['user']['id']
    print "User ID currently in session:", user_id
    messages_query = "SELECT messages.message, messages.id, CONCAT_WS(' ', users.first_name, users.last_name) AS 'user_name', DATE_FORMAT(messages.created_at, '%M %d, %Y') AS 'created_at' FROM messages JOIN users ON messages.user_id = users.id ORDER BY created_at DESC"
    messages= mysql.query_db(messages_query)
    comments_query = "SELECT comments.comment, comments.id, CONCAT_WS(' ', users.first_name, users.last_name) as 'user_name', DATE_FORMAT(comments.created_at, '%M %d, %Y') AS 'created_at', message_id FROM comments JOIN messages ON comments.message_id = messages.id JOIN users on comments.user_id=users.id"
    comments=mysql.query_db(comments_query)
    return render_template('wall.html', messages = messages, comments=comments)

@app.route("/message", methods=["POST"])
def message():
    add_message_query= "INSERT INTO messages(user_id, message, created_at, updated_at) VALUES (:id, :message, NOW(), NOW())"
    data={
        "id": session['user']['id'],
        "message": request.form['message']
    }
    addmsg=mysql.query_db(add_message_query, data)
    return redirect('/wall')

@app.route("/comment/<id>", methods=["POST"])
def comment(id):
    add_comment_query = "INSERT INTO comments(user_id, message_id, comment, created_at, updated_at) VALUES (:id, :message_id, :comment, now(), now())"
    data={
        "id": session['user']['id'],
        "message_id": id,
        "comment": request.form['comment']
    }
    mysql.query_db(add_comment_query, data)
    return redirect('/wall')

@app.route("/clear", methods=["POST"])
def clear():
    session.clear()
    return redirect("/")

app.run(debug=True)

##other add-ons:
##  flash messages for minimum char to POST
##  allow user to delete his/her own message
##  ^^ within 30 mins
##  password requirements
##   style and format
