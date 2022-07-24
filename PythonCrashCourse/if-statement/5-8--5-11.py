list = ['Adam', 'Andrzej', 'Tomek', 'admin', 'Szymon']


if list:
    for name in list:
        if name == 'admin':
            print('hello admin')
        else:
            print(f'Hello user {name}')
else:
    print('There are no users in your list')

for i in range(len(list)):
    list.pop()
print('usunięto wszystkich')

if list:
    for name in list:
        if name == 'admin':
            print('hello admin')
        else:
            print(f'Hello user {name}')
else:
    print('There are no users in your list')

current_users = ['Piotr', 'Wojtek', 'Damian', 'Aleksandra']
new_users = ['Katarzyna', 'Wojtek', 'DAMIAN', 'Kacper']
current_users2 = []

for i in current_users:
    current_users2.append(i.lower())

print(current_users2)

for i in new_users:
    if i.lower() in current_users2:
        print('Wybierz inna nazwe')
    else:
        print('Nazwa jest dostępna')

