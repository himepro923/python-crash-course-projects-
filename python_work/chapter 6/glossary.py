programeing_terms = {
    'list': 'is were you stores values',
    'diconatys': 'is were you store info',
    'value': 'is were you hold a string or number',
    'boolin': 'is were you hold a ture or false',
    'for': 'is for to loop one my one',
    'sorted': 'is to sort by frist letter',
    'if': 'is to loop until something is true',
    '.title': 'is to make the frist litter in a word captial',
    '.upper': 'is to make all letters captial',

}

# print(f'a list {programeing_terms["list"]}')
# print(f'a diconatys {programeing_terms["diconatys"]}')
# print(f'a value {programeing_terms["value"]}')
# print(f'a boolin {programeing_terms["boolin"]}')

for name, value in sorted(programeing_terms.items()):
    print(f'a {name.title()} {value.title()}')
