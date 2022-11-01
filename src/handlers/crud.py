from database.models import Student, Group, db, Course
from flask import request
from flask_restful import Resource, Api, fields, marshal_with, reqparse

api = Api()

resource_fields = {
    'id': fields.Integer,
    'group_id': fields.String,
    'first_name': fields.String,
    'last_name': fields.String,
}


class LessGroup(Resource):

    def get(self):
        dict = {}
        all_group = Group.query.all()
        for group in all_group:
            all_students = Student.query.filter_by(group_id=group.name).all()
            if len(all_students) == 0:
                continue
            dict[group.name] = len(all_students)
        min_number_students = min(dict.values())
        group = {}
        for key, value in dict.items():
            if value == min_number_students:
                group[key] = value

        return group, 200


class Students(Resource):
    @marshal_with(resource_fields, envelope='resource')
    def get(self):
        name = request.args.get('name')
        student_list = []
        for student in Student.query.filter_by(group_id=name).all():
            student_list.append(student)

        return student_list

    @marshal_with(resource_fields)
    def post(self):
        if request.is_json:
            parser = reqparse.RequestParser()
            parser.add_argument("FirstName")
            parser.add_argument("LastName")
            parser.add_argument("GroupId")
            params = parser.parse_args()
            new_student = Student(first_name=params['FirstName'],
                                  last_name=params['LastName'],
                                  group_id=params['GroupId'], )
            db.session.add(new_student)
            db.session.commit()
            return new_student
        else:
            return {'error': 'Request must be JSON'}, 404

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
    parser.add_argument("Name")
    parser.add_argument("LastName")
    parser.add_argument("Course")

    def post(self):
        params = self.parser.parse_args()
        student = Student.query.filter_by(first_name=params["Name"], last_name=params["LastName"]).first()
        current_course = Course.query.filter_by(name=params["Course"]).first()
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
        current_course = Course.query.filter_by(name=params["Course"]).first()
        try:
            student.following.remove(current_course)
            db.session.commit()
            return f'{current_course.name} is deleted', 200
        except ValueError:
            return {'error': 'course not found'}, 404
