# app.py
from flask import Flask
from resources import UserResource
from models import db

app = Flask(__name__)
app.config.from_pyfile('config.py')
db.init_app(app)

api = Api(app)
api.add_resource(UserResource, '/user/<int:user_id>')

if __name__ == '__main__':
    app.run(debug=True)
