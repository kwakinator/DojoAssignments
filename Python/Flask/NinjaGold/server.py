from flask import Flask, render_template, session, request, redirect
import random
from datetime import datetime

app=Flask(__name__)
app.secret_key="yek_terces"

now = datetime.now()

@app.route('/')
def index():
    if "gold" not in session:
        session['gold'] = 0
    if "log" not in session:
        session['log']= []
    return render_template('index.html')

@app.route('/process_money', methods=["POST"])
def process_money():
    temp = {
        'building': request.form['building'],
        'gold': session['gold'],
        'time': now.strftime('%Y/%m/%d %H:%M %p'),
        'earnings': 0
    }
    if temp['building']=='farm':
        temp['earnings']=random.randrange(10,21)
    elif temp['building']=='cave':
        temp['earnings']=random.randrange(5,11)
    elif temp['building']=='house':
        temp['earnings']=random.randrange(2,6)
    elif temp['building']=='casino':
        temp['earnings']=random.randrange(-50,50)

    temp['gold']+=temp['earnings']
    session['gold']=temp['gold']
    session['log'].append(temp)
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

app.run(debug=True)
