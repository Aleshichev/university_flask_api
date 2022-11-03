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
    api.add_resource(LessGroup, '/api/v1/group')
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
        response = self.client.get('/api/v1/group?number=28')
        assert response.status_code == 200

    def test_add_group(self):
        data = {
            "Name": "zq-87"
        }
        response = self.client.post('/api/v1/group', json=data)
        assert response.status_code == 200

    def test_delete_group(self):
        """id - связан с студентами"""
        number = 3
        response = self.client.delete(f'/api/v1/group?id={number}')
        assert response.status_code == 200

    def test_student(self):
        id = 3
        response = self.client.get(f'/api/v1/students?id={id}')
        assert response.status_code == 200

    def test_add_student(self):
        data = {
            "FirstName": "Stiven",
            "LastName": "Spilberg",
            "GroupId": "8"
        }
        response = self.client.post('/api/v1/students', json=data)
        assert response.status_code == 200

    def test_put_student(self):
        id = "5"
        data = {
            "FirstName": "Stiven",
            "LastName": "Spilberg",
            "GroupId": "8"
        }
        response = self.client.put(f'/api/v1/students?id={id}', json=data)
        assert response.status_code == 201

    def test_delete_student(self):
        number = 100
        response = self.client.delete(f'/api/v1/students?id={number}')
        assert response.status_code == 200

    def test_student_to_course(self):
        data = {
            "Name": "Donald",
            "LastName": "Smith",
            "Id": "1"
        }
        response = self.client.post('/api/v1/students/course', json=data)
        assert response.status_code == 200

    def test_delete_student_from_course(self):
        data = {
            "Name": "Donald",
            "LastName": "Smith",
            "Id": "1"
        }
        response = self.client.delete('/api/v1/students/course', json=data)
        assert response.status_code == 200


if __name__ == '__main__':
    unittest.main()
