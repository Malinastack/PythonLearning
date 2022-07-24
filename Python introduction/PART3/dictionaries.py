D1 = dict(id=1, dane=dict(imie='Szymon', nazwisko='Malinowski'))
D2 = dict(wiek=24, zawod='Ślusarz', staz=4)
print(D1['dane']['imie'])

print(D1)
print(D1)
print(D1)
print(D1)
print(D1)
print(D1)
print('imie' in D1)
print(list(D1['dane'].keys())) # aby wyświetlić klucze w postaci listy nalezy uzyc metody list(dict.keys()) poniewaz
# samo dict.keys() zwraca nam obiekt iterowalny a nie gotowa liste
print(list(D1.items())) # zwraca nam liste tupli (klucz, wartosc)
print(list(D2.items()))

print(D1.get('numer')) # get zwraca None jeśli klucz nie istnieje
# print(D1['numer']) # tutaj natomiast uzyskamy KeyError
D3 = dict(imie='Andrzej', nazwisko='Roztocki')
D2.update(D3) # dodaje do konca slownika kolejne pary klucz:wartosc
print(D2)

# kluczem slownika moga byc wszystkie struktury niemutowalne (lancuchy znakow, krotki, liczby)
# np.
D4 = {(2,3,4): 10, (5,6,7): 11}

print(list(D4.items()))

D5 = dict(zip(D1.keys(), D1.values()))
print(D5)

D6 = {x: x**2 for x in [1,2,3,4]}
print(D6)

D7 = {x: x*4 for x in 'Jajko'}
print(D7)


D8 = dict(a=1, b=2, c=3)

K = D8.keys() # klucze slownika zachowuja sie tak jak zbiory (set)
V = D8.values() # wartosci juz nie, poniewaz nie zawsze sa unikatowe lub niemutowalne

# przyklady

print(K | {'d': 4})
print(K & {'b': 10})


# sortowanie kluczy w dict

D9 = dict(d=4, c=3, a=1, b=2, e=5)

print(D9)

D9keys_list = list(D9.keys())
D9keys_list.sort()

for k in D9keys_list:
    print(k, D9[k])


print('Inny sposob sortowania')

D9 = dict(d=4, c=3, a=1, b=2, e=5)

D9keys_list_v2 = list(D9.keys())

for k in sorted(D9keys_list_v2):
    print(k, D9[k])


D9 = dict(d=4, c=3, a=1, b=2, e=5, f={'key': 'value'})

print(sorted(D9)) # a to najszybszy sposób i jedyny wlasciwy !!!!!!!!!!!!!!!!!!!!!!!

for k in sorted(D9):
    print(k, D9[k])

print(*D9.values())

print(list(D9.values()))
print(list(D9.keys()))
print(list(D9.items()))

D10 = dict(d=4, c=3, a=1, b=2, e=5, f=10)

for k, v in sorted(D10.items()):
    print(k, ':', v)
