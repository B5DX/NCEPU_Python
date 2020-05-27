#!/usr/bin/python
# -*- coding: UTF-8 -*-
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
# bootstrap是前端美化的框架
app = Flask(__name__)
app.config.from_object('myconfig')

db = SQLAlchemy(app)
class User(db.Model):
    # 表名
    __tablename__ = 'message_board'

    id = db.Column(db.INTEGER(), primary_key=True)
    content = db.Column(db.String(511))
    name = db.Column(db.String(20))
    time = db.Column(db.DATETIME())
    is_deleted = db.Column(db.INTEGER())

# def models2dict(models):
#     pass

@app.route('/')
def home():
    users = db.session.query(User).all() # 返回对象的tuple
    users = [(u.name, u.content, u.time) for u in users]
    return render_template('users.html', usr_list=users)

if __name__ == '__main__':
    app.run(debug=True)