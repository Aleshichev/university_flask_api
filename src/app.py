from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost/university'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

migrate = Migrate(app, db)

from handlers.create_data import user_cli

app.cli.add_command(user_cli)

if __name__ == "__main__":
    app.run(debug=True)
