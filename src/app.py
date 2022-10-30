from flask import Flask
from flask_migrate import Migrate
from handlers.crud import LessGroup, Students, StudentToCourse

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
    api.add_resource(LessGroup, '/api/v1/group/less')
    api.add_resource(Students,  '/api/v1/students')
    api.add_resource(StudentToCourse, '/api/v1/students/course')
    api.init_app(app)
    return app


if __name__ == "__main__":
    create_app().run(debug=True)
