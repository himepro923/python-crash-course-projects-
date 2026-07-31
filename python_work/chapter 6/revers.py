rivers = {
    'Tigris': 'iraq',
    'Euphrates': 'iraq',
    'Nile': 'egypt',
}

for name, contry in sorted(rivers.items()):
    print(f'{name} runs throgh {contry}')

print()

for river in sorted(rivers.keys()):
    print(river)

print()

for contry in sorted(rivers.values()):
    print(contry)

