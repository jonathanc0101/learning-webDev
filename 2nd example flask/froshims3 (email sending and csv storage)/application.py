from flask import Flask, render_template, request, redirect
from flask_cors import CORS

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import csv
from pathlib import Path

app = Flask(__name__)
CORS(app)

dorms = ["Apley court", "Manhattan", "Etcetera", "Etc."]

filename = Path("./data/registered.csv")


@app.route("/")
def index():
    return render_template("index.html", dorms = dorms)

@app.route("/registrants")
def showRegistrants():
    return render_template("registrants.html", students = loadStudents())

@app.route("/register", methods = ["POST"])
def register():
    name = request.form.get("name")
    dorm = request.form.get("dorm")

    email = request.form.get("email")

    if not name or not dorm or not email:
        return render_template("failure.html")
    else:
        writeCsv(name, dorm, email)
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

def writeCsv(name, dorm, email):
    with open(filename, "a") as file:
        writer = csv.writer(file)
        writer.writerow((name,dorm,email))

def loadStudents():
    students = []

    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row != []:
                students.append(row)

    listOfStudentStrings = ["{name} from {dorm}".format(name = row[0], dorm = row[1]) for row in students]

    return listOfStudentStrings

if __name__ == "__main__":
    app.run(debug=True)