##How does flask know which function to run?
##if we go to local host 5000, in our server-- every function is associated with /___
    ##**look through all of the patterns when you receive a request
    ##the function that is related to the route has to come immediately after it.

##GET:gets information from the server
    #links and redirects

##POST: requests SEND information to the server
    ##secure- not part of the URL
    ##forms package
    ##forms package up information for us in an envelope and deliver it on a 'wire'
    #form action ='/users' method='post'
        #here our wire is the route /users

#Jinja2 Is Our Engine, You are the Driver
index.html

<ul>
{% for item in my_list %}
    <li>{{item}}</li>
{% endfor %}
</ul>


server.py
def index():
strings = ['hi', 'wowie', 'hmm']
##strings=*a database call to retrieve data*
return render_template(index.html, my_list=strings)

can create a form pretty straighforward:

@app.route("/dojo/new", methods=["POST"])
def new():
    print(request.form)
    print (request.form['text'])
    return redirect('/')

#session is unique : user id, whether they are logged in or not
#interacts like it is a dictionary
##as soon as we pull in sessions-- it is encrypted for user security. It is a token (or a packet of data as it is sent back and forth). in order to encrypt them properly-- the secret key and sent across
##Flash messages only exit for one 
