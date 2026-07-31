cities = {
    'baghdad': {
        'loction': 'iraq',
        'population': '9,780,429',
        'fact': 'Baghdad is the capital and largest city in Iraq',
    },
    'new york': {
        'loction': 'usa',
        'population': '8,804,190',
        'fact': 'New York, often called New York City (NYC),[b] is the most populous city in the United States',
    },
    'shatra': {
        'loction': 'iraq',
        'population': '254,000',
        'fact': 'Al-Shatrah (also known as Shatrat al-Muntafiq) is a town in southern Iraq, located north of Nasiriyah',
    }
}

for city, info in cities.items():
    print(f'{city.title()} Location: {info['loction']}, Population: {info['population']}, Fact: {info['fact']}')
