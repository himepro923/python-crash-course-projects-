users = []

for user in users:
    if 'admin' == user:
        print('hello admin whould you like a status report')
    else:
        print(f'hello {user}')
    
if not users:
    print('we need users')

