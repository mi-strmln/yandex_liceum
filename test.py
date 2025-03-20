from requests import get, post, delete, put

print(put('http://localhost:5000/api/jobs/1',
          json={'job': 'deployment of residential module 2'}).json())  # корректный запрос

print(put('http://localhost:5000/api/jobs/1',
          json={}).json())  # некорректный (пустой) запрос
print(put('http://localhost:5000/api/jobs/150',
          json={'job': 'deployment of residential module 2'}).json())  # некорректный (с несуществующим id) запрос
print(put('http://localhost:5000/api/jobs/с',
          json={'job': 'deployment of residential module 2'}).json())  # некорректный (с неверным форматом id) запрос
print(put('http://localhost:5000/api/jobs/150',
          json={'leader_id': 1}).json())  # некорректный (с неверным именем поля) запрос

print(get('http://localhost:5000/api/jobs').json())
