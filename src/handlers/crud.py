from database.models import Student, Group, db, Course
from flask import jsonify, request, make_response
from flask_restful import Resource
from flask_restful import Api

api = Api()


class LessStudent(Resource):

    def get(self):
        dict = {}
        all_group = Group.query.all()
        for group in all_group:
            all_students = Student.query.filter_by(group_id=group.name).all()
            if len(all_students) == 0:
                continue
            dict[group.name] = len(all_students)
        min_number_students = min(dict.values())
        list_group = {}
        for key, value in dict.items():
            if value == min_number_students:
                list_group[key] = value

        return jsonify(list_group)


class Groups(Resource):

    def get(self):
        name = request.args.get('name')
        all_students = Student.query.filter_by(group_id=name).all()
        print(all_students)
        return jsonify(students=[student.to_dict() for student in all_students])


class AddStudent(Resource):

    def post(self):
        if request.is_json:

            new_student = Student(first_name=request.json['FirstName'],
                                  last_name=request.json['LastName'],
                                  group_id=request.json['GroupId'], )
            db.session.add(new_student)
            db.session.commit()
            return make_response(jsonify({'id': new_student.id,
                                          'first_name': new_student.first_name,
                                          'last_name': new_student.last_name,
                                          'group_id': new_student.group_id
                                          }), 201)
        else:
            return {'error': 'Request must be JSON'}, 404


class DeleteStudent(Resource):
    def delete(self, id):
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



class DeleteStudentFromCourse(Resource):
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


