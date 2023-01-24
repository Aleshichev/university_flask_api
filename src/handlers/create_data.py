from database.models import Student, db, Group, Course
from handlers.generate_data import random_group, courses, random_students
from flask.cli import AppGroup
import random

user_cli = AppGroup('user')



@user_cli.command('add_data_group')
def add_data_group():
    group_list = random_group()
    for i in range(len(group_list)):
        new_group = Group(name=group_list[i])
        db.session.add(new_group)
        db.session.commit()


@user_cli.command('add_data_courses')
def add_data_courses():
    for i in range(len(courses)):
        new_course = Course(name=courses[i], description="some_description")
        db.session.add(new_course)
        db.session.commit()


@user_cli.command('add_data_student')
def add_data_student():
    students_list = random_students()
    all_group = Group.query.all()
    try:
        for group in all_group:
            student_to_group = random.sample(students_list, random.randint(20, 30))
            i = 0
            for student in student_to_group:
                name = students_list[i].split(" ")[0]
                l_name = students_list[i].split(" ")[1]
                some_group = group.id
                new_course = Student(first_name=name,
                                     last_name=l_name, group_id=some_group)
                i += 1
                students_list.remove(student)
                db.session.add(new_course)
                db.session.commit()
    except IndexError:
        pass


@user_cli.command('mix_student_courses')
def mix_student_courses():
    all_students = Student.query.all()
    all_courses = Course.query.all()
    for student in all_students:
        courses = random.sample(all_courses, random.randint(1, 3))
        for course in courses:
            student.following.append(course)
            db.session.add(student)
            db.session.commit()
