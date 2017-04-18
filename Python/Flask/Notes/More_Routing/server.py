from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key= "secret hey hey hey"
@app.route("/")
def index():
    return render_template("index.html")
    try:
        name = session['name']
    except KeyError:
        session['name']= 'defaultName'

    or name = session.get('name')

    or try:
        #something that might break
        my_var = session['high_score']
    except: #errorname
        #if it broke, this is the code you want to execute
        print ("it broke.")
        session['high_score'] = 0
    print (session['name'])

@app.route("/users", methods=["POST"])
def create_user():
    print "Got Post Info"
    name = request.form['name']
    email = request.form['email']
    username =session["name"]
    session['name']= "Michael"
    if len(request.form['text']) <1:
        #send an error message
        flash('hey, you need to fill out your name on the form')
    else:
        session['name']= request.form['text']
    session['high_score']+=50
    return redirect("/")
app.run(debug=True)
