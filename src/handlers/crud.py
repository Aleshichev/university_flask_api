from database.models import Student, Group, db, Course
from flask import request
from flask_restful import Resource, Api, fields, marshal_with

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

            new_student = Student(first_name=request.json['FirstName'],
                                  last_name=request.json['LastName'],
                                  group_id=request.json['GroupId'], )
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
    def post(self):
        name = request.args.get('name')
        last_name = request.args.get('lastname')
        course = request.args.get('course')
        student = Student.query.filter_by(first_name=name, last_name=last_name).first()
        currrent_course = Course.query.filter_by(name=course).first()
        try:
            student.following.append(currrent_course)
            db.session.add(student)
            db.session.commit()
            return f'{student.first_name} {student.last_name} is add', 200
        except AttributeError:
            return {'error': 'student not found'}, 404

    def delete(self):
        name = request.args.get('name')
        last_name = request.args.get('lastname')
        course = request.args.get('course')
        student = Student.query.filter_by(first_name=name, last_name=last_name).first()
        currrent_course = Course.query.filter_by(name=course).first()
        try:
            student.following.remove(currrent_course)
            db.session.commit()
            return f'{currrent_course.name} is deleted', 200
        except ValueError:
            return {'error': 'course not found'}, 404
