promet = '\nenter a topping you like'
promet += '\ntype quit to exit: '

what_user_want = []

message = ''

while True:
    message = input(promet)
    what_user_want.append(message)
    print(what_user_want)

    if message == 'quit':
        break

