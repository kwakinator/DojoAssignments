from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
mysql = MySQLConnector(app,'fullfriendsdb')
app.secret_key= 'yek_terces'
EMAILREG= re.compile(r'^[a-zA-Z0-9.+-_]+@[a-zA-Z0-9._-]+\.[a-zA-Z]*$')


@app.route('/')
def index():
    query = "SELECT * FROM friends"     #define your query
    friends = mysql.query_db(query)     # run query with query_db()
    return render_template('index.html', all_friends = friends) #pass data to our template

@app.route('/friends', methods=["POST"])
def create():
    data = {
             'first_name': request.form['first_name'],
             'last_name':  request.form['last_name'],
             'email': request.form['email']
           }
    if len(data['first_name'])<2:
        flash('First name must be at least 2 characters')
    if len(data['last_name'])<2:
        flash('Last name must be at least 2 characters')
    if not EMAILREG.match(data['email']):
        flash('Please enter a valid email address')
    if '_flashes' in session:
        return redirect('/')
    query = "INSERT INTO friends (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW())"
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/friends/<id>/edit', methods=["GET"])
def edit(id):
    query = "SELECT id, first_name, last_name, email FROM friends WHERE id = :id"
    data = {'id': id}
    one_friend = mysql.query_db(query, data)
    return render_template('edit.html', friend=one_friend[0])

@app.route('/friends/<id>', methods=["POST"])
def update(id):
    query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, email = :email WHERE id = :id"
    data = {
             'first_name': request.form['first_name'],
             'last_name':  request.form['last_name'],
             'email': request.form['email'],
             'id': id
           }
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/friends/<id>/check', methods=["GET"])
def deletecheck(id):
    query = "SELECT id, first_name, last_name, email FROM friends WHERE id = :id"
    data = {
        'id': id
    }
    delete_friend = mysql.query_db(query, data)
    return render_template('delete.html', friend=delete_friend[0])

@app.route('/friends/<id>/delete', methods=["POST"])
def destroy(id):
    query = "DELETE FROM friends WHERE id = :id"
    data = {'id': id}
    mysql.query_db(query, data)
    flash('Friend Information has been deleted')
    return redirect('/')

app.run(debug=True)
