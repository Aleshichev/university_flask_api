from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

student_courses = db.Table('student_courses',
                           db.Column('student_id', db.Integer, db.ForeignKey('students.id')),
                           db.Column('course_id', db.Integer, db.ForeignKey('courses.id'))
                           )


class Group(db.Model):
    __tablename__ = 'groups'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<group: {self.name}>"


class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    group_id = db.Column(db.String(50))
    first_name = db.Column(db.String(50), nullable=True)
    last_name = db.Column(db.String(50), nullable=True)
    following = db.relationship('Course', secondary=student_courses, backref="followers")

    def __repr__(self):
        return f"<student: {self.first_name} {self.last_name}>"


class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    description = db.Column(db.String(500), nullable=True)

    def __repr__(self):
        return f"<course: {self.name} - {self.description}>"
