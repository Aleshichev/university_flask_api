# Flask SQL
### This is a simple application can insert/select/update/delete data in the database using sqlalchemy and flask rest framework.

Database has 3 tables:

Groups
Courses
Students
The application accepts the following requests:

/api/v1/groups - all groups with numbers of students. GET method has an optional parameter "number_of_students", it returns groups less than or equal to parameter's value.

/api/v1/students - all students with their group and list of courses. GET method has an optional parameter "course_name", it returns all students who has this parameter's value in their list of courses. In the POST method and DELETE method you can add new student or remove existing student.

/api/v1/courses - all courses with their description and list of students who are enrolled in this course. Using the POST method you can enroll a student in a course and using the DELETE method you can remove a student from the course.



##Command-line interface 
 
