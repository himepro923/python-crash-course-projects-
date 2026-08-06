respones = {}

polling_active = True

while polling_active:
    name = input('What you name: ')
    moutin = input('What mountin whould you like to climb some day: ')

    respones[name] = moutin

    repet = input('Whould you like to go agen: (yes/no) ')
    if repet == 'no':
        break

print(respones)

 
