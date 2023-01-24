from database.models import Student, Group, db, Course
from flask import request
from flask_restful import Resource, fields, marshal_with, reqparse
from sqlalchemy import func

students_fields = {
    'id': fields.Integer,
    'group_id': fields.String,
    'first_name': fields.String,
    'last_name': fields.String,
}

group_fields = {
    'id': fields.Integer,
    'name': fields.String,
}


class LessGroup(Resource):

    def get(self):
        number = request.args.get('number')
        groups = Student.query.with_entities(Student.group_id).\
            group_by(Student.group_id).\
            having((func.count(Student.id)) <= number).all()

        group_list = []
        for group in groups:
            group_list.append(*group)

        return group_list, 200

    @marshal_with(group_fields, envelope='group')
    def post(self):
        if request.is_json:
            parser = reqparse.RequestParser()
            parser.add_argument("Name")
            params = parser.parse_args()
            new_group = Group(name=params["Name"])
            db.session.add(new_group)
            db.session.commit()
            return new_group
        else:
            return {'error': 'Request must be JSON'}, 404

    def delete(self):
        id = request.args.get('id')
        group = Group.query.get(id)
        if group is None:
            return {'error': 'not found'}, 404
        db.session.delete(group)
        db.session.commit()
        return f'{id} is deleted', 200


class Students(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("FirstName", type=str, required=True)
    parser.add_argument("LastName", type=str, required=True)
    parser.add_argument("GroupId", type=int, required=True)

    @marshal_with(students_fields, envelope='students')
    def get(self):
        id = request.args.get('id')
        student_list = []
        for student in Student.query.filter_by(group_id=id).all():
            student_list.append(student)

        return student_list

    @marshal_with(students_fields, envelope='students')
    def post(self):
        if request.is_json:

            params = self.parser.parse_args()
            new_student = Student(first_name=params['FirstName'],
                                  last_name=params['LastName'],
                                  group_id=params['GroupId'], )
            db.session.add(new_student)
            db.session.commit()
            return new_student
        else:
            return {'error': 'Request must be JSON'}, 404

    @marshal_with(students_fields, envelope='students')
    def put(self):
        id = request.args.get('id')
        student = Student.query.get(id)
        params = self.parser.parse_args()
        student.group_id = params['GroupId']
        student.last_name = params['LastName']
        student.first_name = params['FirstName']

        db.session.commit()
        return student, 201

    def delete(self):
        id = request.args.get('id')
        student = Student.query.get(id)
        if student is None:
            return {'error': 'not found'}, 404
        db.session.delete(student)
        db.session.commit()
        return f'{id} is deleted', 200


class StudentToCourse(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("Name", type=str, required=True)
    parser.add_argument("LastName", type=str, required=True)
    parser.add_argument("Id", type=int, required=True)

    def post(self):
        params = self.parser.parse_args()
        student = Student.query.filter_by(first_name=params["Name"], last_name=params["LastName"]).first()
        current_course = Course.query.filter_by(id=params["Id"]).first()
        try:
            student.following.append(current_course)
            db.session.add(student)
            db.session.commit()
            return f'{student.first_name} {student.last_name} is add', 200
        except AttributeError:
            return {'error': 'student not found'}, 404

    def delete(self):
        params = self.parser.parse_args()
        student = Student.query.filter_by(first_name=params["Name"], last_name=params["LastName"]).first()
        current_course = Course.query.filter_by(id=params["Id"]).first()
        try:
            student.following.remove(current_course)
            db.session.commit()
            return f'{current_course.name} is deleted', 200
        except ValueError:
            return {'error': 'course not found'}, 404
