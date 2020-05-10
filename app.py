from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
	render_this = "Hi whoever is this!!"
	return render_template("webpage.html", headline=render_this)

if __name__=="__main__":
    app.run(debug=True)