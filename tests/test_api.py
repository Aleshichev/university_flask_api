import unittest
from flask import Flask
from database.models import db
from handlers.crud import LessGroup, Students, StudentToCourse


def create_app():
    app = Flask(__name__)
    # app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:123@localhost/test_db"
    app.config["TESTING"] = True
    db.init_app(app)
    from handlers.crud import api
    api.add_resource(LessGroup, '/api/v1/group/less')
    api.add_resource(Students, '/api/v1/students')
    api.add_resource(StudentToCourse, '/api/v1/students/course')
    api.init_app(app)
    return app

class TestMain():

    def setup(self):
        self.app = create_app()
        self.app.testing = True
        self.client = self.app.test_client()

    def test_group(self):
        response = self.client.get('/api/v1/students?name=qq-80')
        assert response.status_code == 200

    def test_less_student(self):
        response = self.client.get('/api/v1/group/less')
        assert response.status_code == 200

    def test_add_student(self):
        data = {
            "FirstName": "Stiven",
            "LastName": "Spilberg",
            "GroupId": "qs-89"
        }
        response = self.client.post('/api/v1/students', json=data)
        assert response.status_code == 200

    def test_delete_student(self):
        number = 100
        response = self.client.delete(f'/api/v1/students?id={number}')
        assert response.status_code == 200

    def test_student_to_course(self):
        data = {
            "Name": "Peggy",
            "LastName": "Burris",
            "Course": "Chemistry"
        }
        response = self.client.post('/api/v1/students/course', json=data)
        assert response.status_code == 200

    def test_delete_student_from_course(self):
        data = {
            "Name": "Peggy",
            "LastName": "Burris",
            "Course": "Chemistry"
        }
        response = self.client.delete('/api/v1/students/course', json=data)
        assert response.status_code == 200


if __name__ == '__main__':
    unittest.main()
