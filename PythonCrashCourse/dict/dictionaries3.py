pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}

print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")
for topping in pizza['toppings']:
    print(f"\t{topping}")

person1 = {'name': 'Kasia', 'last_name': 'Kulmaczewska', 'age': '22',  'City': 'Olsztyn'}
person2 = {'name': 'Andrzej', 'last_name': 'Sobieszwski', 'age': '25',  'City': 'Warszawa'}
person3 = {'name': 'Tomasz', 'last_name': 'Sikora', 'age': '27',  'City': 'Łódź'}

people_list = [person1, person2, person3]

for i in people_list:
    for k, v in i.items():
        print(f'{k.title()}: {v.title()}')
    print('\n')

favorite_places = {
    'Andrzej': ['Dubai', 'Iran', 'Egypt'],
    'Tomasz': ['Ełk', 'Giżycko', 'Warszawa'],
    'Asia': ['Tatry', 'Mount Everest', 'Sudety']
}

for k, v in favorite_places.items():
    print(f'Hello {k} your favourite places are:')
    for i in v:
        print(i)

cities = {
    'Warsaw': {},
    'Poznań': {},
    'Olsztyn': {}
}

cities['Warsaw'] = {'population': '2mln', 'area': '10km2'}
cities['Poznań'] = {'population': '1mln', 'area': '5km2'}
cities['Olsztyn'] = {'population': '160tys', 'area': '3km2'}

for cities, city_info in cities.items():
    print(f'{cities}: ')
    for keys, values in city_info.items():
        print(f'{keys}: {values}')

