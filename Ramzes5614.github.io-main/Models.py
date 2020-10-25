from app import db
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


#Модель для маршрута
class Road(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    datatime = db.Column(db.DateTime, default=datetime.utcnow)
    address_id = db.Column(db.Integer,db.ForeignKey('address.id'))
    comment = db.relationship('Comment', backref='road', lazy=True)
    coord = db.relationship('Road_Coords', backref='road_of_coord', uselist=False ,lazy=True)


#Модель для примечаний по маршруту
class Comment(db.Model):
    comment_Id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Numeric)
    type = db.Column(db.String(128))
    longitude = db.Column(db.Numeric)
    datatime = db.Column(db.DateTime, default=datetime.utcnow)
    road_id = db.Column(db.Integer, db.ForeignKey('road.id'))

#Модель для адресов и координат
class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(128))
    street = db.Column(db.String(128))
    house = db.Column(db.String(128))
    description = db.Column(db.Text(255))
    latitude = db.Column(db.Numeric)
    longitude = db.Column(db.Numeric)
    roads = db.relationship('Road', backref='address', lazy=True)

#Для хранения координат маршрута
class Road_Coords(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    latitude =db.Column(db.Numeric)
    longitude = db.Column(db.Numeric)
    road = db.Column(db.Integer, db.ForeignKey('road.id'))