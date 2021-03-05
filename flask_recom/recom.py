from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
# import numpy as np
# import pickle
# import pandas as pd
# import os

recom = Flask(__name__)
recom.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(recom)

class Recommend(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __rep__(self):
        return '<Task %r>' % self.id

# #define route
# @recom.route('/')
# #create controller
# def index():
#     return render_template('index.html')
#
# @recom.route('/Price')
# #price button on controller
#
# @recom.route('/Mileage')
# #mileage button on controller
#
# @recom.route('/CMV')
# #cmv button

if __name__ == '__main__':
    recom.run(debug=True)
