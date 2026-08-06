promet = '\nPlese enter the name of the city you vitesd'
promet += '\ntype "quit" when done: '

while True:
    city = input(promet)

    if city == 'quit':
        break
    else:
        print(f'i whould love to vist {city}')
