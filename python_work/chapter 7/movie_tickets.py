promet = '\nWhat is you age for the movie tickets'
promet += '\ntype quit to exit: '

while True:
    message = int(input(promet))
    if message < 3:
        print('tickets are free')
    elif message <= 12:
        print('tickets are $10')
    elif message > 12:
        print('tickets are $15')
    if message == 'quit':
        break
