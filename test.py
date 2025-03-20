from requests import get, post, delete


print(delete('http://localhost:5000/api/jobs/3').json())
print(get('http://localhost:5000/api/jobs').json())

