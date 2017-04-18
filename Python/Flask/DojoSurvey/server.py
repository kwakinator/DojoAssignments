from flask import Flask, render_template, request, redirect

app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=["GET", "POST"])
def create_user():
    print "Got Post Info"
    print(request.form)
    if request.method=="POST":
        name = request.form['name']
        location = request.form['location']
        language = request.form['language']
        comment = request.form['comment']
        return render_template("result.html", name = name, location = location, language = language, comment = comment)
    return redirect("/result")
app.run(debug=True)
