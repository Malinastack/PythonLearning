dict = {'name': 'Kasia', 'last_name':'Kulmaczewska', 'age': 22,  'City': 'Olsztyn'}

for k, v in dict.items():
    print(k + ": " + str(v))


dict2 = {'Andrzej': 10, 'Kasia': 7, 'Tomek': 12}

print(f'Andrzeja ulubiony numer to {dict2["Andrzej"]}')


dict3 = {'nile': 'egypt', 'wisla': 'poland', 'amazon': 'south-america'}

for k, v in dict3.items():
    print(f'{k.title()} runs through {v.title()}')

for k in dict3:
    print(k)

for v in dict3.values():
    print(v)


favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

people = ['adam', 'konrad', 'jen', 'sarah', 'edward', 'phil']

for person in people:
    print(f'Hello {person}')
    if person in favorite_languages.keys():
        print(f'Thanks for taking part in a poll {person}')
    elif person not in favorite_languages.keys():
        print(f'You should take part in poll {person}')
