from database.models import Student, db, student_courses
from flask import jsonify, request
from flask_restful import Resource
from flask_restful import Api
from handlers.create_data import mix_student

api = Api()


class LessOrEquals(Resource):

    def get(self):
        mix = mix_student()
        print(mix)
        # list=[]
        # for student in mix_student():
        #     list.append(student)
        # return jsonify(list)
        # students = student_courses.query.all()
        # name = request.args.get('name')
        # print(name)
        # return jsonify(all_students=[student.to_dict() for student in students])

#
# class Add(Resource):
#
#     def add_student(self):
#
#         # group_id = "201"
#         # last_name = "Donald"
#         # new_student = Student(group_id=group_id, first_name=name, last_name=last_name)
#         # db.session.add(new_student)
#         # db.session.commit()
