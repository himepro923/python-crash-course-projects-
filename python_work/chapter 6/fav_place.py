favorite_places = {
    'hasan': ['baghdad', 'tokyo'],
    'hikmat': ['london'],
    'ali': ['rome', 'paris', 'cairo'],
}

for name, place in favorite_places.items():
    place = ", ".join(place)
    print(f'{name.title()} fav place is {place}')