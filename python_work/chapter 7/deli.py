sandwich_orders = ['Reuben', 'Club Sandwich', 'Philly Cheesesteak',]

finished_sandwichs = []

while sandwich_orders:
    transstion_sandwich = sandwich_orders.pop()

    print(f'\nComplited {transstion_sandwich}')

    finished_sandwichs.append(transstion_sandwich)

print()

print(finished_sandwichs)
