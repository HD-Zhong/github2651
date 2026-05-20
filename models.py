from flask_sqlalchemy import SQLAlchemy

# 初始化SQLAlchemy，后续在app.py中绑定app
db = SQLAlchemy()

# 学生模型 包含 id/姓名/年龄/性别/专业 字段
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))
    major = db.Column(db.String(50))




