from requests import get, post, delete, put

print(get('http://localhost:5000/api/v2/jobs/1').json())  # Корректный запрос
print()
print(get('http://localhost:5000/api/v2/jobs/12').json())  # Некорректный (с несуществующим id) запрос
print()
print(get('http://localhost:5000/api/v2/jobs/').json())  # Некорректный (с пустым id) запрос
print()
print(get('http://localhost:5000/api/v2/jobs/с').json())  # Некорректный (с неверным форматом id) запрос
print()

print(post('http://localhost:5000/api/v2/jobs', json={  # Корректный запрос
    'team_leader': 1,
    'job': 'training interns',
    'work_size': 5,
    'collaborators': '2',
    'is_finished': False
}).json())
print()
print(post('http://localhost:5000/api/v2/jobs', json={  # Некорректный (с неполным числом полей) запрос
    'team_leader': 1,
    'job': 'training interns',
    'collaborators': '2',
    'is_finished': False
}).json())
print()
print(post('http://localhost:5000/api/v2/jobs', json={}).json())  # Некорректный (пустой) запрос
print()
print(post('http://localhost:5000/api/v2/jobs', json={  # Некорректный (с неверным именем поля) запрос
    'leader_id': 1,
    'job': 'training interns',
    'work_size': 5,
    'collaborators': '2',
    'is_finished': False
}).json())
print()

print(delete('http://localhost:5000/api/v2/jobs/2').json())  # Корректный запрос
print()
print(delete('http://localhost:5000/api/v2/jobs/').json())  # Некорректный (с пустым id) запрос
print()
print(delete('http://localhost:5000/api/v2/jobs/900').json())  # Некорректный (с несуществующим id) запрос
print()
print(delete('http://localhost:5000/api/v2/jobs/с').json())  # Некорректный (с неверным форматом id) запрос
print()

print(get('http://localhost:5000/api/v2/jobs').json())  # Корректный запрос
