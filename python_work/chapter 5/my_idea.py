user_level = ''

title_level = ["Novice", "Warrior", "Legend"]

print(f'there are 100 levels see your ranks from {title_level}')

if user_level == 'Novice':
    print('you can acces levels 1-25')
elif user_level == 'Warrior':
    print('you can acces levels 25-75')
elif user_level == 'Legend':
    print('you can acces levels 75-100')
else:
    print('play the danm game')