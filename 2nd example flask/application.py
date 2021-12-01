from flask import Flask, render_template, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods = ["POST"])
def register():
    name = request.form.get("name")
    dorm = request.form.get("dorm")

    if not name or not dorm:
        return "FAILURE"
    else:
        render_template("success.html")
    ##to-do: implement database access

if __name__ == "__main__":
    app.run(debug=True)