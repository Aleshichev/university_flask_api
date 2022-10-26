from flask import Flask
from flask_migrate import Migrate
from handlers.crud import LessStudent, Groups, AddStudent, DeleteStudent, DeleteStudentFromCourse, StudentToCourse

migrate = Migrate()


def create_app():
    """Application-factory pattern"""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost/university'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    from database.models import db
    db.init_app(app)

    from handlers.create_data import user_cli
    app.cli.add_command(user_cli)

    migrate.init_app(app, db)

    from handlers.crud import api
    api.add_resource(LessStudent, '/api/v1/group/less')
    api.add_resource(Groups, '/api/v1/group')
    api.add_resource(AddStudent, '/api/v1/student')
    api.add_resource(DeleteStudent, '/api/v1/student/delete/<int:id>')
    api.add_resource(DeleteStudentFromCourse, '/api/v1/student/delete')
    api.add_resource(StudentToCourse, '/api/v1/student/add')
    api.init_app(app)
    return app


if __name__ == "__main__":
    create_app().run(debug=True)
