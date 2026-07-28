from flask import current_app as app
from flask import render_template, request, redirect, url_for
from models import *

#Define all routes here

@app.route("/")
def home():
    return "Hello HMS"

@app.route("/login", methods=["GET","POST"])
def signin():
    #check user_credentials, if admin redirect to admin dash_board
    if request.method=="POST":
        uname=request.form.get("emailid")
        pwd=request.form.get("password")
        user=db.session.query(User_Credentials).filter(User_Credentials.email==uname, User_Credentials.password==pwd).first()
        if user and user.role == 0:
            return redirect(url_for("admin_dashboard"))
        else:
            return redirect(url_for("signup"))
    return render_template("login.html")


@app.route("/register", methods=["GET","POST"]) 
def signup():
    if request.method=="POST":
        uname=request.form.get("emailid")
        pwd=request.form.get("pwd")
        role=request.form.get("utype")
        user=db.session.query(User_Credentials).filter(User_Credentials.email==uname).first()#check existance
        #need to store in user credentials
        if user:
            return render_template('signup.html', err_msg="Sorry email already in use!")
        else:
            uc=User_Credentials(email=uname, password=pwd, role=int(role))
            db.session.add(uc)
            db.session.commit() #save in db

    #request type is get
    return render_template("signup.html")

#data dict
app_dct=[
    {"SrNo":"1","p_name":"xyz", "d_name":"abc", "spz":"Neurology"},
    {"SrNo":"2","p_name":"pqr", "d_name":"cdf", "spz":"Cardiology"},
]

@app.route("/admin")
def admin_dashboard():
    return render_template("admin_dashboard.html", app_data =app_dct)


@app.route("/patient_details")
def patient_details():
    return render_template("patient_details.html")

@app.route("/patient")
def patient_dashboard():
    return render_template("patient_dashboard.html")

@app.route("/doctor")
def doctor_dasboard():
    return render_template("doctor_dashboard.html")

