from requests import get, post

#print(get('http://localhost:5000/api/jobs').json())
#print(get('http://localhost:5000/api/jobs/1').json())
#print(get('http://localhost:5000/api/jobs/100').json())
#print(get('http://localhost:5000/api/jobs/f').json())
print(post('http://localhost:5000/api/jobs',
           json={'team_leader': 1,
                 'job': 'equipment check',
                 'work_size': 24,
                 'collaborators': '2, 3',
                 'is_finished': False}).json())
