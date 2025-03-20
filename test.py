from requests import get, post, delete, put


print(put('http://localhost:5000/api/jobs/1', json={
            'job': 'deployment of residential module 2'
        }).json())

print(get('http://localhost:5000/api/jobs').json())

