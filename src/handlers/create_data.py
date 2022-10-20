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
    # while i < len(students_list)-1:
    # while i < 10:
    try:
        for group in all_group:
                student_to_group = random.sample(students_list, random.randint(20, 30))
                i = 0
                print(len(students_list))
                for student in student_to_group:
                    name = students_list[i].split(" ")[0]
                    l_name = students_list[i].split(" ")[1]
                    some_group = group
                    new_course = Student(id=i, first_name=name,
                                         last_name=l_name, group_id=some_group)
                    i += 1
                    students_list.remove(student)
                    print(f"{new_course.id} - {new_course.group_id} - {new_course.first_name} - {new_course.last_name}")
                    print(len(students_list))
                    # db.session.add(new_course)
                    # db.session.commit()
    except IndexError:
        pass




@user_cli.command('mix_student')
def mix_student():
    all_students = Student.query.all()
    all_group = Group.query.all()
    for group in all_group:
        student_to_group = random.sample(all_students, random.randint(20, 30))
        for student in student_to_group:
            student_name = student.first_name
            student_second_name = student.last_name
            group_r = group.name
            # print(f"{student_name} {student_second_name} {group_r}")
            new_data = Student(group_id=group_r,
                               first_name=student_name,
                               last_name=student_second_name)
            print(new_data.group_id)
            db.session.add(new_data)
            db.session.commit()
        # dict[group] = student_to_group
        # print(dict)


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
