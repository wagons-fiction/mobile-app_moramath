# resources.py
from flask_restful import Resource, reqparse
from models import User

parser = reqparse.RequestParser()
parser.add_argument('username', type=str, help='Username')
parser.add_argument('email', type=str, help='Email')

class UserResource(Resource):
    def get(self, user_id):
        user = User.query.filter_by(id=user_id).first()
        if user:
            return {'username': user.username, 'email': user.email}
        else:
            return {'message': 'User not found'}, 404

    def put(self, user_id):
        args = parser.parse_args()
        user = User.query.filter_by(id=user_id).first()
        if user:
            user.username = args['username']
            user.email = args['email']
            db.session.commit()
            return {'message': 'User updated successfully'}
        else:
            return {'message': 'User not found'}, 404

    def delete(self, user_id):
        user = User.query.filter_by(id=user_id).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return {'message': 'User deleted successfully'}
        else:
            return {'message': 'User not found'}, 404
