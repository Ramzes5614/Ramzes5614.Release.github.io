from flask import Flask, render_template
from flask_restful import Api
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import random

app = Flask(__name__)
app.config.from_object(Configuration)
api = Api(app)

db = SQLAlchemy(app)


# connect = mysql.connector.connect(user='User', password='user', host='localhost', database = 'Post_Address')
    #def __init__(self, **kwords):
     #   super(Addres, self).__init__(**kwords)






