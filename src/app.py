from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

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
        return f"<group: {self.id}>"


class Student(db.Model):
    __tablename__ = 'students'
    group_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=True)
    last_name = db.Column(db.String(50), nullable=True)

    def __init__(self, name):
        self.group_id = 'group_id'
        self.first_name = 'first_name'
        self.last_name = 'last_name'

    def __repr__(self):
        return f"<student: {self.id}>"


class Course(db.Model):
    __tablename__ = 'courses'
    name = db.Column(db.String(50), unique=True, primary_key=True)
    description = db.Column(db.String(500), nullable=True)

    def __init__(self, name):
        self.name = 'name'
        self.description = 'description'

    def __repr__(self):
        return f"<course: {self.id}>"

#
# with app.app_context():
#     db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
