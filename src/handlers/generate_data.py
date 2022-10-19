import random
import string
from random import choice
import names

"""
+ 10 групп со случайно сгенерированными именами. Имя должно содержать 2 символа, дефис, 2 цифры
+ Создать 10 курсов (математика, биология и т. д.)
+ 200 студентов. Возьмите 20 имен и 20 фамилий и случайным образом скомбинируйте их, чтобы получить учеников.
4. Случайным образом распределите учащихся по группам. В каждой группе могло быть от 10 до 30 студентов. Возможно, что какие-то группы будут без студентов или студенты без групп
5. Создайте отношение MANY-TO-MANY между таблицами STUDENTS и COURSES. Случайным образом назначить от 1 до 3 курсов для каждого студента

"""
courses = ["Matematic", "Algebra", "Biology", "Drawing", "Chemistry", "Geography", "Geometry", "History", "Literature",
           "Physics"]


def random_letter():
    letter = choice(string.ascii_lowercase)
    return letter


def random_naumber():
    number = choice(string.digits)
    return number


def random_group():
    group_list = []
    for i in range(10):
        group_list.append(f"{random_letter()}{random_letter()} - {random_naumber()}{random_naumber()}")
    return group_list


def first_name():
    first_name_list = []
    for i in range(10):
        first_name_list.append(f"{names.get_first_name(gender='female')}")
        first_name_list.append(f"{names.get_first_name(gender='male')}")
    return first_name_list


def last_name():
    last_name_list = []
    for i in range(20):
        last_name_list.append(f"{names.get_last_name()}")
    return last_name_list


def random_students():
    students_list = []
    for i in range(200):
        students_list.append(f"{random.choice(first_name())} {random.choice(last_name())}")
    return students_list



