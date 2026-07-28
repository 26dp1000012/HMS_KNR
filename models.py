from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User_Credentials(db.Model):
    __tablename__='user_credentials' # user define table name
    id=db.Column(db.Integer, primary_key=True)
    email=db.Column(db.String, unique=True, nullable=False)
    password=db.Column(db.String, nullable=False)
    role=db.Column(db.Integer, nullable=False) # allowed admin/ doctor/ patient
    patients= db.Relationship("Pt_Profile", cascade="all,delete", backref="user_credentials")#relation linking parent to child. Ex:wlinking to patient profile.
    doctors= db.Relationship("Dr_Profile", cascade="all,delete", backref="user_credentials")#relation linking parent to child. Ex:wlinking to doctor profile.

class Pt_Profile(db.Model):
    __tablename__='pt_profile'
    id=db.Column(db.Integer, primary_key=True)
    pt_id=db.Column(db.Integer, db.ForeignKey("user_credentials.id"), nullable=False)# linking child to parent
    fullname=db.Column(db.String, unique=True, nullable=False)
    address=db.Column(db.String, nullable=False)
    phone_num=db.Column(db.String, nullable=False)
    status=db.Column(db.Integer, nullable=False, default=0) #0-registered, 1-deactivated
  
class Dr_Profile(db.Model):
    __tablename__='dr_profile'
    id=db.Column(db.Integer, primary_key=True)
    dr_id=db.Column(db.Integer, db.ForeignKey("user_credentials.id"), nullable=False)
    fullname=db.Column(db.String, unique=True, nullable=False)
    address=db.Column(db.String, nullable=False)
    phone_num=db.Column(db.String, nullable=False)
    spl=db.Column(db.String, nullable=False)
    experiance=db.Column(db.Float, nullable=False)
    status=db.Column(db.Integer, nullable=False, default=0) #0-registered, 1-approved, 2-deactivated