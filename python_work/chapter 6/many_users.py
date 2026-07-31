users = {
    'hasan_pro': {
        'frist': 'hasan',
        'last': 'hikamt',
        'location': 'iraq',
    },
    'hikmat_pro': {
        'frist': 'hikmat',
        'last': 'hikmat',
        'location': 'usa',
    },
}
for username, user_info in users.items():
    print(f'\n Username: {username}')
    print(f'\n Full info: frist: {user_info['frist']}, last: {user_info['last']}')
    print(f'loction: {user_info['location']}')