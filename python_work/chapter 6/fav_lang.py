fav_lang = {
    'hasan': ['java', 'rust'],
    'hussam': ['c', 'C++'],
    'jawad': ['python', 'c#'],
    'hikmat' : ['go'],
}


for name, lang in fav_lang.items():
    lang = ' '.join(lang)
    if len(lang) == 2:
        print(f'{name.title()} fav lang is {lang}')
    elif len(lang) > 2:
        print(f'{name} fav langs are \n{lang}')
