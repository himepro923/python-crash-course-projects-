dog = {
    'name': 'bob',
    'owner': 'bobs owner',
}

cat = {
    'name': 'meow',
    'owner': 'meow owner',
}

fish = {
    'name': 'blop',
    'owner': 'blop owner',
}

brid = {
    'name': 'twet',
    'owner': 'twet owner',
}

snail = {
    'name': 'slide',
    'owner': 'slide owner',
}

lizerd = {
    'name': 'clime',
    'owner': 'clime owner',
}

snake = {
    'name': 'slither',
    'owner': 'slither owner',
}


all_anmials = [dog, cat, fish, brid, snail, lizerd, snake]

for anmial in all_anmials:
    print(f'Name: {anmial['name']}, Owner: {anmial['owner']}')