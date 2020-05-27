from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    # 表名
    __tablename__ = 'message_board'

    id = db.Column(db.INTEGER(), primary_key=True)
    content = db.Column(db.String(511))
    name = db.Column(db.String(20))
    time = db.Column(db.DATETIME())
    is_deleted = db.Column(db.INTEGER())
