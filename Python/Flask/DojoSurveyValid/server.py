from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key= "yek_terces"

@app.route('/')
def index():
    if "users" not in session:
        session['users']=[]
    return render_template("index.html")


@app.route('/result', methods=["POST"])
def addUser():
    user= {
        "name" : request.form['name'],
        "location" : request.form['location'],
        "language" : request.form['language'],
        "comment" : request.form['comment']
    }

    if len(user['name']) < 1:
        flash("Name cannot be empty!")
    if len(user['comment']) < 1:
        flash("Comment field cannot be empty!")
    if len(user['comment'])>120:
        flash("120 character limit please!")

    if "_flashes" in session:
        return redirect('/')

    session['user']= user
    session['users'].append(user)
    return render_template("result.html")

@app.route('/clear')
def clearSession():
    session.clear()
    return redirect('/')

app.run(debug=True)
