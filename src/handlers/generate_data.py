import random
import string
from random import choice
import names

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
        group_list.append(f"{random_letter()}{random_letter()}-{random_naumber()}{random_naumber()}")
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
