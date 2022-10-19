from database.models import Student
from flask import jsonify
from flask_restful import Resource



class Main(Resource):

    def get(self):
        students = Student.query.all()
        return jsonify(all_students=[student.to_dict() for student in students])
