sandwich_orders = ['Reuben', 'Club Sandwich', 'Philly Cheesesteak', 'pastrami', 'pastrami', 'pastrami', 'pastrami', 'pastrami']

finished_sandwichs = []

print('\nWe have ran out of pastrami')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    transstion_sandwich = sandwich_orders.pop()

    print(f'\nComplited {transstion_sandwich}')

    finished_sandwichs.append(transstion_sandwich)

print()

print(finished_sandwichs)
