from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Student

# 蓝图：彻底解决 404 + 循环导入
bp = Blueprint('main', __name__)

# 首页
@bp.route('/')
@bp.route('/index')
def index():
    search = request.args.get('search', '')
    if search:
        students = Student.query.filter(
            Student.name.like(f'%{search}%') | Student.major.like(f'%{search}%')
        ).all()
    else:
        students = Student.query.all()
    return render_template('index.html', students=students, search=search)

# 添加
@bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        gender = request.form.get('gender')
        major = request.form.get('major')
        new_stu = Student(name=name, age=age, gender=gender, major=major)
        db.session.add(new_stu)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('add.html')

# 编辑
@bp.route('/edit/<int:sid>', methods=['GET', 'POST'])
def edit(sid):
    stu = Student.query.get_or_404(sid)
    if request.method == 'POST':
        stu.name = request.form.get('name')
        stu.age = request.form.get('age')
        stu.gender = request.form.get('gender')
        stu.major = request.form.get('major')
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('edit.html', stu=stu)

# 删除
@bp.route('/delete/<int:sid>')
def delete(sid):
    stu = Student.query.get_or_404(sid)
    db.session.delete(stu)
    db.session.commit()
    return redirect(url_for('main.index'))

# 批量删除
@bp.route('/batch_delete', methods=['POST'])
def batch_delete():
    id_list = request.form.getlist('ids')
    if id_list:
        Student.query.filter(Student.id.in_(id_list)).delete()
        db.session.commit()
    return redirect(url_for('main.index'))