from requests import get, post


print(post('http://localhost:5000/api/jobs',
           json={'team_leader': 1,
                 'job': 'air analysis',
                 'work_size': 10,
                 'collaborators': '2',
                 'is_finished': False}).json()) # корректный запрос
print()
print(post('http://localhost:5000/api/news', json={}).json()) # некорректный (пустой) запрос
print()
print(post('http://localhost:5000/api/news',
           json={'team_leader': 2}).json()) # некорректный (с не полным набором полей) запрос
print()
print(post('http://localhost:5000/api/jobs',
           json={'team_lider': 1,
                 'job': 'air analysis',
                 'work_size': 10,
                 'collaborators': '2',
                 'is_finished': False}).json()) # некорректный (с неправильным назанием поля) запрос

print()
print(get('http://localhost:5000/api/jobs').json())

