#good practice to call the main file app.py

from os import truncate
from flask import Flask, render_template, request
from flask_cors import CORS

from models import createPost, getPosts

app = Flask(__name__)

CORS(app)

@app.route("/", methods = ["GET", "POST"])
def index():

    if request.method == "GET":
        pass

    if request.method == "POST":
        name = request.form.get("name")
        post = request.form.get("post")
        
        createPost(name, post)

    postsGotten = getPosts()
    return render_template("index.html", posts = postsGotten)

if __name__ == "__main__":
    app.run(debug=True)