from flask import Flask, make_response, jsonify, redirect, render_template
from data import db_session, jobs_api, users_api
from flask_login import LoginManager
import requests
import os

from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    session = db_session.create_session()
    return session.query(User).get(user_id)


@app.errorhandler(400)
def bad_request(_):
    return make_response(jsonify({'error': 'Bad Request'}), 400)


@app.errorhandler(404)
def not_found(_):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/users_show/<int:user_id>')
def show_user_city(user_id):
    user = requests.get(f'http://localhost:5000/api/users/{user_id}').json()
    if 'error' in user:
        return redirect('/')
    user = user['user']
    p = {
        'geocode': user['city_from'],
        'apikey': '3f098ecf-c589-46fa-b6ac-6b4cc84a704a',
        'format': 'json',
        'results': 1
    }
    response = requests.get('http://geocode-maps.yandex.ru/1.x/', params=p).json()
    response = response['response']['GeoObjectCollection']['featureMember']
    if not len(response):
        return 'Город не найден'
    response = response[0]['GeoObject']
    coord = tuple(map(float, response['Point']['pos'].split()))
    print(coord)
    p = {
        'l': 'sat',
        'll': ','.join(map(str, coord)),
        'z': 10
    }
    response = requests.get('https://static-maps.yandex.ru/1.x/', params=p)

    path = 'static/img'
    os.makedirs(path, exist_ok=True)

    file_path = os.path.join(path, 'hometown.png')
    with open(file_path, 'wb') as f:
        f.write(response.content)

    return render_template(
        'users_show.html',
        title='Hometown',
        user=user,
        photo='/static/img/hometown.png'
    )


def main():
    db_session.global_init("db/mars_explorer.db")
    app.register_blueprint(jobs_api.blueprint)
    app.register_blueprint(users_api.blueprint)
    app.run()


if __name__ == '__main__':
    main()
