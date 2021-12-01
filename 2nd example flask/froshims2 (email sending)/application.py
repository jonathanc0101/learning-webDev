from flask import Flask, render_template, request, redirect
from flask_cors import CORS

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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

    email = request.form.get("email")

    if not name or not dorm or not email:
        return render_template("failure.html")
    else:
        students.append("{student} from {dorm}".format(student = name, dorm = dorm))

        sendMail(name,dorm,email)

        return redirect("/registrants")
    
def sendMail(name,dorm,email):
    #mail info
    message = "Congratulations {name} you are registered!".format(name = name)
    # create message object instance
    msg = MIMEMultipart()
    # setup the parameters of the message
    pssa = "jonathancaviaTestjonathancaviaTest"
    msg['From'] = "jonathancaviatest@gmail.com"
    msg['To'] = email
    msg['Subject'] = "Congratulations for signing up to froshims2!"

    # add in the message body
    msg.attach(MIMEText(message, 'plain'))

    #create server
    server = smtplib.SMTP('smtp.gmail.com: 587')

    server.starttls()
    # Login Credentials for sending the mail
    server.login(msg['From'], pssa)
    
    # send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())

    server.quit()

if __name__ == "__main__":
    app.run(debug=True)