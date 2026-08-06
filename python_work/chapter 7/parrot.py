proment = '\ntell me something and i will repet it to you'
proment += '\n type quit to stop the programe '

active = True

while active:
    message = input(proment)

    if message == 'quit':
        active = False
    else:
        print(message)
