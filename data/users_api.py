from datetime import datetime
import flask
from flask import jsonify, request, Blueprint, make_response
from data import db_session
from data.users import User

blueprint = Blueprint('users_api', __name__, template_folder='templates')


@blueprint.route('/api/users')
def get_users():
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
                'modified_date',
                'city_from'
            )) for item in users]
        }
    )


@blueprint.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    session = db_session.create_session()
    user = session.query(User).get(user_id)
    if user:
        return jsonify(
            {
                'user': user.to_dict(only=(
                    'id',
                    'name',
                    'surname',
                    'age',
                    'position',
                    'speciality',
                    'address',
                    'email',
                    'modified_date',
                    'city_from'
                ))
            }
        )
    return make_response(jsonify({'error': 'Not Found'}, 404))


@blueprint.route('/api/users', methods=['POST'])
def create_user():
    if not request.json:
        return make_response(jsonify({'error': 'Empty request'}), 400)
    elif not all(key in request.json for key in
                 ['id', 'name', 'surname', 'age', 'position', 'speciality', 'address', 'email']):
        return make_response(jsonify({'error': 'Bad request'}), 400)
    session = db_session.create_session()
    if session.query(User).get(request.json['id']):
        return jsonify({'error': 'Id already exists'})
    user = User(
        id=request.json['id'],
        name=request.json['name'],
        surname=request.json['surname'],
        age=request.json['age'],
        position=request.json['position'],
        speciality=request.json['speciality'],
        address=request.json['address'],
        email=request.json['email']
    )
    session.add(user)
    session.commit()
    return jsonify({id: user.id})


@blueprint.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    session = db_session.create_session()
    user = session.query(User).get(user_id)
    if not user:
        return jsonify({'error': 'Not found'})
    session.delete(user)
    session.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/users/<int:user_id>', methods=['PUT'])
def edit_user(user_id):
    if not request.json:
        return make_response(jsonify({'error': 'Empty request'}), 400)
    session = db_session.create_session()
    user = session.query(User).get(user_id)
    if not user:
        return make_response(jsonify({'error': 'Bad request'}), 404)
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
    user.modified_date = datetime.now()
    session.commit()
    return jsonify({'success': 'OK'})
