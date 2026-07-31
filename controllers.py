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
        elif user and user.role == 1:
            return redirect(url_for("doctor_dashboard"))
        elif user and user.role == 2:
            return redirect(url_for("patient_dashboard"))
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
            #After credntials then separate pt and Dr
            fname=request.form.get("fname")
            address=request.form.get("address")
            phone_num=request.form.get("phone_num")
            if int(role)==2:
                pt_profile = Pt_Profile(pt_id=uc.id,fullname=fname,address=address, phone_num=phone_num)
                db.session.add(pt_profile)#if patient role
            else:
                splz=request.form.get("splz")
                exp=request.form.get("exp")
                dr_profile=Dr_Profile(dr_id=uc.id,fullname=fname,address=address, phone_num=phone_num, spl=splz,experiance=exp)
                db.session.add(dr_profile)#if doctor role
            db.session.commit()
    else:
        #request type is get
        return render_template("signup.html")#Save everything


@app.route("/admin")
def admin_dashboard():
    dr_data = get_all_drs()
    pt_data = get_all_pts()
    return render_template("admin_dashboard.html", dr_data=dr_data, pt_data=pt_data)
                           
@app.route("/patient_details")
def patient_details():
    return render_template("patient_details.html")

@app.route("/patient")
def patient_dashboard():
    return render_template("patient_dashboard.html")

@app.route("/doctor")
def doctor_dashboard():
    return render_template("doctor_dashboard.html")

@app.route("/ed_dr")
def edit_doctor():
    #render with specific doctor data
    dr_id=request.args.get("dr_id")
    dr_searched=search_dr(dr_id)
    return render_template("edit_doctor.html", dr_data=dr_searched)

@app.route("/update_dr", methods=['GET','POST'])
def update_dr():
    uid=request.form.get("uid")
    name=request.form.get("d_name")
    splz=request.form.get("splz")
    exp=request.form.get("exp")
    address=request.form.get("address")
    old_dr_details = db.session.query(Dr_Profile).filter(Dr_Profile.dr_id==uid).first()
    print(old_dr_details)
    #update
    old_dr_details.fullname=name
    old_dr_details.spl=splz
    old_dr_details.exp=exp
    old_dr_details.address=address
    db.session.commit()
    return redirect(url_for("admin_dashboard"))

#Additional python function:
def get_all_drs():
    dr_data=db.session.query(Dr_Profile).filter().all()
    return dr_data

def get_all_pts():
    pt_data=db.session.query(Pt_Profile).filter().all()
    return pt_data

def search_dr(id):
    dr_searched=db.session.query(Dr_Profile).filter(Dr_Profile.dr_id==id).first()
    return dr_searched
 