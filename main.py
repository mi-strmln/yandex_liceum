from flask import Flask, render_template, redirect
from data import db_session
from data.users import User
from data.jobs import Jobs
from data.forms import RegisterForm, LoginForm, WorksForm, WorksRedactionForm
from flask_login import login_user, logout_user, login_required, current_user, LoginManager
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(id)


@app.route("/")
def journal_works():
    session = db_session.create_session()
    jobs = session.query(Jobs).all()
    return render_template("journal_works.html", title='List of Jobs', jobs=jobs)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.confirm.data:
            return render_template('register.html', title='Registration',
                                   form=form,
                                   message="Passwords don't match")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.login.data).first():
            return render_template('register.html', title='Registration',
                                   form=form,
                                   message="This user already exists")
        user = User(
            name=form.name.data,
            email=form.login.data,
            surname=form.surname.data,
            age=form.age.data,
            position=form.position.data,
            speciality=form.speciality.data,
            address=form.address.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Registration', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Wrong email or password",
                               form=form)
    return render_template('login.html', title='Authorisation', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/addjob', methods=['GET', 'POST'])
def add_work():
    form = WorksForm()
    if form.submit.data:
        db_sess = db_session.create_session()
        job = Jobs(
            team_leader=form.team_leader.data,
            creator=current_user.id,
            job=form.job.data,
            work_size=form.work_size.data,
            collaborators=form.collaborators.data,
            is_finished=form.is_finished.data
        )
        db_sess.add(job)
        db_sess.commit()
        return redirect('/')
    return render_template('add_job.html', title='Adding Job', form=form, type='Adding a job')


@app.route('/redact_job/<int:job_id>', methods=['GET', 'POST'])
def redact_job(job_id):
    form = WorksRedactionForm()
    if form.submit.data:
        db_sess = db_session.create_session()
        if current_user.id != 1:
            job = db_sess.query(Jobs).filter(Jobs.id == job_id, Jobs.creator == current_user.id).first()
        else:
            job = db_sess.query(Jobs).filter(Jobs.id == job_id).first()
        if job:
            job.team_leader = form.team_leader.data if form.team_leader.data else job.team_leader
            job.job = form.job.data if form.job.data else job.job
            job.work_size = form.work_size.data if form.work_size.data else job.work_size
            job.collaborators = form.collaborators.data if form.collaborators.data else job.collaborators
            job.is_finished = form.is_finished.data if form.is_finished.data else job.is_finished
            db_sess.commit()
            return redirect('/')
    return render_template('add_job.html', title=f'Redacting Job: {job_id}', form=form, type='Redacting')


def main():
    db_session.global_init("db/mars_explorer.db")
    app.run()


if __name__ == '__main__':
    main()
