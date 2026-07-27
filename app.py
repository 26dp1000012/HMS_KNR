from flask import Flask, render_template
from controllers import *

app = Flask(__name__ )


@app.route("/")
def home():
    return "Hello HMS"

@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/signup")
def signup():
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


#executable of flask
if __name__ == "__main__":
    app.run(debug=True)
