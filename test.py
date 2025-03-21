from requests import get, post, delete, put

print(get('http://localhost:5000/api/v2/users/1').json())  # Корректный запрос
print()
print(get('http://localhost:5000/api/v2/users/12').json())  # Некорректный (с несуществующим id) запрос
print()
print(get('http://localhost:5000/api/v2/users/').json())  # Некорректный (с пустым id) запрос
print()
print(get('http://localhost:5000/api/v2/users/с').json())  # Некорректный (с неверным форматом id) запрос
print()

print(post('http://localhost:5000/api/v2/users', json={  # Корректный запрос
    'name': 'ann',
    'surname': 'black',
    'age': 21,
    'position': 'employee',
    'speciality': 'biolog',
    'address': 'module2',
    'email': 'annb@mars.ru'
}).json())
print()
print(post('http://localhost:5000/api/v2/users', json={  # Некорректный (с неполным числом полей) запрос
    'name': 'ann',
    'surname': 'black',
    'age': 21,
    'email': 'annb@mars.ru'
}).json())
print()
print(post('http://localhost:5000/api/v2/users', json={}).json())  # Некорректный (пустой) запрос
print()
print(post('http://localhost:5000/api/v2/users', json={  # Некорректный (с неверным именем поля) запрос
    'name': 'ann',
    'surname': 'black',
    'age': 21,
    'post': 'employee',
    'speciality': 'biolog',
    'address': 'module2',
    'email': 'annb@mars.ru'
}).json())
print()

print(delete('http://localhost:5000/api/v2/users/4').json())  # Корректный запрос
print()
print(delete('http://localhost:5000/api/v2/users/').json())  # Некорректный (с пустым id) запрос
print()
print(delete('http://localhost:5000/api/v2/users/900').json())  # Некорректный (с несуществующим id) запрос
print()
print(delete('http://localhost:5000/api/v2/users/с').json())  # Некорректный (с неверным форматом id) запрос
print()

print(get('http://localhost:5000/api/v2/users').json())  # Корректный запрос
