from flask import Flask, render_template, request, redirect, session

app=Flask(__name__)
app.secret_key= "S3cr3ts"


@app.route('/')
def index():
    if "counter" not in session:
        session['counter'] = 0
    else:
        session['counter'] += 1
    return render_template('index.html')

@app.route('/two')
def addTwo():
    session['counter'] += 2
    return render_template('index.html')

@app.route('/clear')
def clear_session():
    session.clear()
    return redirect('/')
app.run(debug=True)
