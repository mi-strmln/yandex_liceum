from flask import Flask, render_template, redirect
from data import db_session
from data.users import User
from data.jobs import Jobs
import datetime

# from forms.user import RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

@app.route("/")
def journal_works():
    session = db_session.create_session()
    jobs = session.query(Jobs).all()
    return render_template("journal_works.html", title='List of Jobs', jobs=jobs)


def main():
    db_session.global_init("db/mars_explorer.db")
    app.run()


if __name__ == '__main__':
    main()
