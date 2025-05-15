from requests import get, post, delete, put

print(get('http://localhost:5000/api/users').json())
print(get('http://localhost:5000/api/users/1').json())
print(post('http://localhost:5000/api/users', json={
            'name': 'Mike',
            'surname': 'White',
            'age': 40,
            'position': '1student',
            'speciality': 'biolog',
            'address': 'module 1',
            'email': 'mwhite@mail.ru',
        }).json())
print(put('http://localhost:5000/api/users/1', json={
            'address': 'new_address'
        }).json())
print(delete('http://localhost:5000/api/users/3').json())
print(get('http://localhost:5000/api/users').json())
