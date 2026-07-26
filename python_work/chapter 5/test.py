avable_toppings = ['mushrooms', 'olives', 'green peper', 'pepoeoni', 'pineapple', 'extra chese']

requsted_toppings = ['mushrooms', 'frinch fries', 'extra chese']

for requsted_topping in requsted_toppings:
    if requsted_topping in avable_toppings:
        print(f'adding {requsted_topping}')
    else:
        print(f'we dont have {requsted_topping}')


