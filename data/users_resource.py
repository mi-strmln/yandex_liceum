from flask_restful import Resource, abort
from flask import jsonify, request
from data import db_session
from data.users import User
from data.reqparse import parser
import datetime


def abort_if_news_not_found(user_id):
    session = db_session.create_session()
    user = session.query(User).get(user_id)
    if not user:
        abort(404, message=f"News {user_id} not found")


class UserResource(Resource):
    def get(self, user_id):
        abort_if_news_not_found(user_id)
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        return jsonify({'user': user.to_dict(
            only=('id',
                  'name',
                  'surname',
                  'age',
                  'position',
                  'speciality',
                  'address',
                  'email',
                  'modified_date'))})

    def put(self, user_id):
        abort_if_news_not_found(user_id)
        session = db_session.create_session()
        if not request.json:
            return jsonify({'error': 'Empty request'})
        user = session.query(User).get(user_id)
        if 'name' in request.json:
            user.name = request.json['name']
        if 'surname' in request.json:
            user.surname = request.json['surname']
        if 'age' in request.json:
            user.age = request.json['age']
        if 'position' in request.json:
            user.position = request.json['position']
        if 'speciality' in request.json:
            user.speciality = request.json['speciality']
        if 'address' in request.json:
            user.address = request.json['address']
        if 'email' in request.json:
            user.email = request.json['email']
        user.modified_date = datetime.datetime.now()
        session.commit()
        return jsonify({'success': 'OK'})

    def delete(self, user_id):
        abort_if_news_not_found(user_id)
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        session.delete(user)
        session.commit()
        return jsonify({'success': 'OK'})


class UserListResource(Resource):
    def get(self):
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify(
            {
                'users': [item.to_dict(only=(
                    'id',
                    'name',
                    'surname',
                    'age',
                    'position',
                    'speciality',
                    'address',
                    'email',
                    'modified_date'
                )) for item in users]
            }
        )

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        user = User(
            name=args['name'],
            surname=args['surname'],
            age=args['age'],
            position=args['position'],
            speciality=args['speciality'],
            address=args['address'],
            email=args['email']
        )
        session.add(user)
        session.commit()
        return jsonify({'id': user.id})
