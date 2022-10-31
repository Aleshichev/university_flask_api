import unittest
from src.app import create_app


class TestMain():

    def setup(self):
        app = create_app()
        app.testing = True
        self.client = app.test_client()

    def test_group(self):
        response = self.client.get('/api/v1/students?name=yj-55')
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
        number = 7
        response = self.client.delete(f'/api/v1/students?id={number}')
        assert response.status_code == 200

    def test_delete_student_from_course(self):
        name = 'Cassandra'
        lastname = 'Flook'
        course = 'Chemistry'
        response = self.client.delete(f'/api/v1/students/course?name={name}&lastname={lastname}&course={course}')
        assert response.status_code == 200

    def test_student_to_course(self):
        name = 'Cassandra'
        lastname = 'Flook'
        course = 'Chemistry'
        response = self.client.post(f'/api/v1/students/course?name={name}&lastname={lastname}&course={course}')
        assert response.status_code == 200


if __name__ == '__main__':
    unittest.main()
