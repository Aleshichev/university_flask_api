from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost/university'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

migrate = Migrate(app, db)

from handlers.create_data import user_cli
from handlers.crud import Main

api = Api()
api.add_resource(Main, '/get')
api.init_app(app)

app.cli.add_command(user_cli)


if __name__ == "__main__":
    app.run(debug=True)
