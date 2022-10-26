from flask_testing import TestCase
import unittest
from database.models import Group, db, Student, Course
from flask import Flask
from handlers.create_data import add_data_group, add_data_courses, add_data_student, mix_student_courses


class MyTestCase(TestCase):

    def create_app(self):
        app = Flask(__name__)
        # app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
        app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:123@localhost/test_db"
        app.config["TESTING"] = True
        db.init_app(app)
        return app

    def setUp(self):
        self.app = self.create_app()
        db.create_all()
        self.client = self.app.test_client()

    # def tearDown(self):
    #     db.session.remove()
    #     db.drop_all()

    def test_db_Group(self):
        db.session.add(Group(name='xz-12'))
        group = Group.query.filter_by(id=1)
        assert group is not None

    def test_db_Student(self):
        db.session.add(Student(first_name='Cristian', last_name="Djons", group_id='tr-34'))
        student = Student.query.filter_by(id=1)
        assert student is not None

    def test_db_Course(self):
        db.session.add(Course(name='Geometry', description="Some description"))
        course = Course.query.filter_by(id=1)
        assert course is not None


    def test_add_data_group(self):
        app = self.create_app()
        runner = app.test_cli_runner()
        result = runner.invoke(add_data_group)
        group = Group.query.filter_by(id=2)
        assert group is not None
        assert '' in result.output

    def test_add_data_courses(self):
        app = self.create_app()
        runner = app.test_cli_runner()
        result = runner.invoke(add_data_courses)
        course = Course.query.filter_by(id=2)
        assert course is not None
        assert '' in result.output

    def test_add_data_student(self):
        app = self.create_app()
        runner = app.test_cli_runner()
        result = runner.invoke(add_data_student)
        student = Student.query.filter_by(id=2)
        assert student is not None
        assert '' in result.output

    def test_mix_student_courses(self):
        app = self.create_app()
        runner = app.test_cli_runner()
        result = runner.invoke(mix_student_courses)
        assert '' in result.output

if __name__ == '__main__':
    unittest.main()
