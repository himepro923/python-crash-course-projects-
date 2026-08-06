places_they_want_to_go = {}

polling_running = True

while polling_running:
    name = input('\nWhats is your name: ')
    place = input('\nWere do you want to go: ')

    places_they_want_to_go[name] = place

    repet = input('\nDo you want to go agien: (yes/no) ')

    if repet == 'no':
        break

print('\n---poll resalts---')

print(places_they_want_to_go)
