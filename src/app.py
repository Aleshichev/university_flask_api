from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from handlers.generate_data import random_group, courses, random_students
import click

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost/university'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

migrate = Migrate(app, db)


class Group(db.Model):
    __tablename__ = 'groups'
    name = db.Column(db.String(50), unique=True, primary_key=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<group: {self.name}>"


class Student(db.Model):
    __tablename__ = 'students'
    group_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=True)
    last_name = db.Column(db.String(50), nullable=True)

    # def __init__(self, name):
    #     self.group_id = 'group_id'
    #     self.first_name = 'first_name'
    #     self.last_name = 'last_name'

    def __repr__(self):
        return f"<student: {self.group_id}>"


class Course(db.Model):
    __tablename__ = 'courses'
    name = db.Column(db.String(50), unique=True, primary_key=True)
    description = db.Column(db.String(500), nullable=True)

    # def __init__(self, name):
    #     self.name = 'name'
    #     self.description = 'description'

    def __repr__(self):
        return f"<course: {self.name}{self.description}>"


@app.cli.command("add_data_group")
def add_data_group():
    group_list = random_group()
    for i in range(len(group_list)):
        new_group = Group(name=group_list[i])
        db.session.add(new_group)
        db.session.commit()


@app.cli.command("add_data_courses")
def add_data_courses():
    for i in range(len(courses)):
        new_course = Course(name=courses[i], description="some_description")
        db.session.add(new_course)
        db.session.commit()


@app.cli.command("add_data_student")
def add_data_student():
    students_list = random_students()
    for i in range(len(students_list)):
        name = students_list[i].split(" ")[0]
        l_name = students_list[i].split(" ")[1]
        number = 1 + i
        new_course = Student(group_id=number, first_name=name,
                             last_name=l_name)
        db.session.add(new_course)
        db.session.commit()


if __name__ == "__main__":
    app.run(debug=True)
