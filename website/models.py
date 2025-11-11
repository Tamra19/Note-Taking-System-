from . import db    #"." is website(package h isliye naam likhne ki need nhi h)
from flask_login import UserMixin   #what is this?
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    #how you associate different notes to different users(relationship between Note and User[foreign key])
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))   #we must pass a valid user_id to access/write notes(oneToMany relationship; one=user, many=notes)

#Learn how to pass media(images, videos) by watching SQLAlchemy tutorial
#learn all types of relationships(one-to-many, many-to-one, many-to-many, one-to-one)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique = True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note') #it will be a list that will store different notes(we are referencing name of the class)
    