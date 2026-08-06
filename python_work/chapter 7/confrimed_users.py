unconfrimed_users = ['hasan', 'hussam', 'hikmat',]
confrimed_users = []

while unconfrimed_users:
    current_user = unconfrimed_users.pop()

    print(f'veryfying new user: {current_user}')
    confrimed_users.append(current_user)

print('\nthe following users have been confermed: ')
for confrimed_user in confrimed_users:
    print(confrimed_user.title())
