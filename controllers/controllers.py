from flask import current_app as app, render_template

#Define all routes here

@app.route("/")
def home():
    return "Hello HMS"

@app.route("/login")
def signin():
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
