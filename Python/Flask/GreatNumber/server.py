from flask import Flask, render_template, request, session, redirect
import random

app=Flask(__name__)
app.secret_key= "yek_terces"

@app.route('/')
def index():
    if "number" not in session:
        session['number'] = random.randrange(0,101)
    print "The number is", session['number']
    return render_template("index.html")

@app.route('/guess', methods= ["POST"])
def result():
    guess = int(request.form['guess'])
    if guess < session['number']:
        print "too low"
        session['guess'] = "low"
    elif guess > session['number']:
        print "too high"
        session['guess'] = "high"
    else:
        print "match"
        session['guess'] = "match"
    return redirect('/')

@app.route('/clear')
def newGame():
    session.pop('guess')
    session.pop('number')
    return redirect('/')
app.run(debug=True)
