import flask
from flask import jsonify, make_response, request
from data import db_session
from data.jobs import Jobs

blueprint = flask.Blueprint('jobs_api', __name__, template_folder='templates')


@blueprint.route('/api/jobs')
def get_jobs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return jsonify(
        {
            'jobs': [item.to_dict(only=(
                'id', 'team_leader', 'job', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished'
            )) for item in jobs]
        }
    )


@blueprint.route('/api/jobs/<int:job_id>', methods=['GET'])
def get_job(job_id):
    db_sess = db_session.create_session()
    job = db_sess.query(Jobs).get(job_id)
    if job:
        return jsonify({
            'job': job.to_dict(only=(
                'id', 'team_leader', 'job', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished'
            ))
        })
    return make_response(jsonify({'error': 'Not found'}, 404))


@blueprint.route('/api/jobs', methods=['POST'])
def add_job():
    if not request.json:
        return make_response(jsonify({'error': 'Empty request'}), 400)
    elif not all(key in request.json for key in
                 ['team_leader', 'job', 'work_size', 'collaborators', 'is_finished']):
        return make_response(jsonify({'error': 'Bad request'}), 400)
    db_sess = db_session.create_session()
    jobs = Jobs(
        team_leader=request.json['team_leader'],
        job=request.json['job'],
        work_size=request.json['work_size'],
        collaborators=request.json['collaborators'],
        is_finished=request.json['is_finished']
    )
    db_sess.add(jobs)
    db_sess.commit()
    return jsonify({'id': jobs.id})


@blueprint.route('/api/jobs/<int:jobs_id>', methods=['DELETE'])
def delete_job(jobs_id):
    db_sess = db_session.create_session()
    job = db_sess.query(Jobs).get(jobs_id)
    if not job:
        return make_response(jsonify({'error': 'Not found'}), 404)
    db_sess.delete(job)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/jobs/<int:job_id>', methods=['PUT'])
def edit_job(job_id):
    if not request.json:
        return make_response(jsonify({'error': 'Empty request'}), 400)
    db_sess = db_session.create_session()
    job = db_sess.query(Jobs).get(job_id)
    if not job:
        return make_response(jsonify({'error': 'Bad request'}), 404)
    if 'team_leader' in request.json:
        job.leader_id = request.json['team_leader']
    if 'job' in request.json:
        job.job = request.json['job']
    if 'work_size' in request.json:
        job.work_size = request.json['work_size']
    if 'collaborators' in request.json:
        job.collaborators = request.json['collaborators']
    if 'is_finished' in request.json:
        job.is_finished = request.json['is_finished']
    db_sess.commit()
    return jsonify({'success': 'OK'})
