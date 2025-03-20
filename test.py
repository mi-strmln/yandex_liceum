from requests import get, post, delete


print(delete('http://localhost:5000/api/jobs/4').json()) # корректный запрос
print(delete('http://localhost:5000/api/jobs/150').json()) # некорректный (с несуществующим id) запрос
print(delete('http://localhost:5000/api/jobs/').json()) # некорректный (пустой) запрос
print(delete('http://localhost:5000/api/jobs/с').json()) # некорректный (с неверным форматом id) запрос

print(get('http://localhost:5000/api/jobs').json())

