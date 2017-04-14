from flask import Flask, render_template, redirect #imports Flask
app = Flask(__name__)   #global variable __name__ tells Flask whether or not we are running the file directly, or importing it as a module.

@app.route('/')         #the "@" symbol designates a "decorator" which attaches the function to the "/" route. Whenever we send a request to localhost:5000/ we will run the hello_world function. we will need this line in every application built in Flask.
def hello_world():
    name = "Harry"
    age = 12
    return render_template('index.html', name = "Harry", age = age)

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/numbers')
def numbers():
    for number in range(3):
        print "we're in number"
    return redirect('/')

app.run(debug = True, port = 8888)
