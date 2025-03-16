from flask import Flask, render_template, redirect
from data import db_session
from data.users import User
from data.jobs import Jobs
import datetime

# from forms.user import RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_explorer.db")
    # app.run()
    cap = User()
    cap.surname = "Scott"
    cap.name = "Ridley"
    cap.age = 21
    cap.position = "captain"
    cap.speciality = "research engineer"
    cap.address = "module_1"
    cap.email = "scott_chief@mars.org"
    db_sess = db_session.create_session()
    db_sess.add(cap)
    db_sess.commit()

    colonist1 = User()
    colonist1.surname = "Cook"
    colonist1.name = "James"
    colonist1.age = 20
    colonist1.position = "captain's assistant"
    colonist1.speciality = "programmer"
    colonist1.address = "module_1"
    colonist1.email = "cook_j@mars.org"
    db_sess = db_session.create_session()
    db_sess.add(colonist1)
    db_sess.commit()

    colonist2 = User()
    colonist2.surname = "Smith"
    colonist2.name = "Jonn"
    colonist2.age = 23
    colonist2.position = "employee"
    colonist2.speciality = "meteorologist"
    colonist2.address = "module_2"
    colonist2.email = "smith_j@mars.org"
    db_sess = db_session.create_session()
    db_sess.add(colonist2)
    db_sess.commit()

    colonist3 = User()
    colonist3.surname = "Watson"
    colonist3.name = "Ashley"
    colonist3.age = 19
    colonist3.position = "intern"
    colonist3.speciality = "roboticist"
    colonist3.address = "module_2"
    colonist3.email = "watson_a@mars.org"
    db_sess = db_session.create_session()
    db_sess.add(colonist3)
    db_sess.commit()

    job1 = Jobs()
    job1.team_leader = 1
    job1.job = "deployment of residential modules 1 and 2"
    job1.work_size = 15
    job1.collaborators = "2, 3"
    db_sess = db_session.create_session()
    db_sess.add(job1)
    db_sess.commit()


if __name__ == '__main__':
    main()
