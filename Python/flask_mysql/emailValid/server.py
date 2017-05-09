from flask import Flask, render_template, redirect, session, flash, request
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
mysql = MySQLConnector(app,'emailvalid')
app.secret_key= 'yek_terces'
EMAILREG= re.compile(r'^[a-zA-Z0-9.+-_]+@[a-zA-Z0-9._-]+\.[a-zA-Z]*$')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success', methods=['POST'])
def success():
    data = {
            'email': request.form['email']
    }
    if EMAILREG.match(data['email']):
        query="INSERT INTO emailvalid(email, created_on, updated_on) VALUES (:email, NOW(), NOW())"
        mysql.query_db(query, data)
        query_all = "SELECT email, created_on FROM emailvalid"
        emails = mysql.query_db(query_all)
        return render_template('success.html', emails=emails, email=data)
    else:
        flash('EMAIL IS NOT VALID.')
        return redirect('/')

app.run(debug=True)
