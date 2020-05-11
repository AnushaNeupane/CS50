
from flask import Flask, render_template, request #represents request made by people in webserver

app = Flask(__name__)


@app.route("/")
def webpage():
	return render_template("webpage.html") # Links url to hello()

@app.route("/hello", methods=["POST"]) 
# /hello is the route
# telling route this method
# this hello() function is called when someone fills the form and click submit 

def hello():
	name = request.form.get("name") # take request, access the form and get part of form ie. name= name from html
	return render_template("hello.html", name=name) # render template from that variable name, getting name from form that user filled out

if __name__ == "__main__":
    app.run(debug=True)
