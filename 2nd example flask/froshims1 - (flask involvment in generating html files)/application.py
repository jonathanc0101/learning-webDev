from flask import Flask, render_template, request
from flask_cors import CORS
from werkzeug.utils import redirect

app = Flask(__name__)
CORS(app)

students = []

dorms = ["Apley court", "Manhattan", "Etcetera", "Etc."]

@app.route("/")
def index():
    return render_template("index.html", dorms = dorms)

@app.route("/registrants")
def showRegistrants():
    return render_template("registrants.html", students = students)

@app.route("/register", methods = ["POST"])
def register():
    name = request.form.get("name")
    dorm = request.form.get("dorm")

    if not name or not dorm:
        return render_template("failure.html")
    else:
        students.append("{student} from {dorm}".format(student = name, dorm = dorm))

        return redirect("/registrants")
    

if __name__ == "__main__":
    app.run(debug=True)