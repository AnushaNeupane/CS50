
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
	names= ["Alice", "Bob", "Candice"]
	return render_template("webpage.html", names=names)

if __name__ == "__main__":
    app.run(debug=True)