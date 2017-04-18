from flask import Flask, render_template, redirect, session, request, flash
import re

app=Flask(__name__)
app.secret_key= "yek_terces"

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

NAME_REGEX=re.compile(r'^[a-zA-Z]*$')

@app.route('/', methods=['GET'])
def index():
    if "users" not in session:
        session['users']=[]
    return render_template('index.html')

@app.route('/login', methods=["POST"])
def submit():
    user={
        "first_name" : request.form['fname'],
        "last_name" :request.form['lname'],
        "email" :request.form['email'],
        "password" :request.form['password'],
        "conpassword" :request.form['conpassword']
    }
    if len(user['first_name'])  < 1 or len(user['last_name'])  < 1 or len(user['email'])  < 1 or len(user['password'])  < 1 or len(user['conpassword']) < 1:
            flash("All fields are required", 'error')

    if not EMAIL_REGEX.match(user['email']):
             flash("Invalid Email Address!", 'error')

    if not NAME_REGEX.match(user['first_name']) or not  NAME_REGEX.match(user['last_name']):
            flash("Letters in your name only!", 'error')

    if len(user['password']) < 9:
            flash("Must be at least 8 characters", 'error')

    if user['conpassword'] != user['password']:
            flash("Passwords do not match, please re-enter", "error")

    if "_flashes" in session:
            return redirect('/')

    session['user']=user
    session['users'].append(user)
    flash("Thanks for submitting!", "success")
    print session['users']
    return render_template('index.html')

@app.route('/clear')
def clearSession():
    session.clear()
    return redirect('/')
app.run(debug=True)
