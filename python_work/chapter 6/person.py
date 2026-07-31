hasan = {
    'name': 'hasan',
    'last name': 'hikmat',
    'city': 'baghdad',
    'age': 15,
}

hikamt = {
    'name': 'hikmat',
    'last name': 'hikmat',
    'city': 'baghdad',
    'age': '12',
}

info_of_users = [hasan, hikamt]

for info in info_of_users:
    print(f'Name: {info['name']}, Last name: {info['last name']}, City: {info['city']}, Age: {info['age']}')
