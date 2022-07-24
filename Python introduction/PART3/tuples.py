from collections import namedtuple
T1 = (1, 2, 3, 4, 2)
T2 = (6, 7)
T3 = (6,)
T4 = (1, 2, 3, [6, 6, 6], 4)
print(T1 + T2)
print(T1 * 4)
print(T1[:3])

print(T1.index(2)) # pierwsze wystąpienie elementu o wartości 2
print(T1.index(2, 2)) # pierwsze wystąpienie elementu o wartości 2 po przesunięciu o 2 pozycje
print(T1.count(2))

# T[1] = 0 nie zadziala, tuple są niemutowalne
T4[3][0] = 2 # ale elementy mutowalne w tuplach mozna zmieniac
print(T4) # (1, 2, 3, [2, 6, 6], 4)

# namedtuples

rec = namedtuple('dane', ['name', 'age', 'jobs'])
adam = rec('Szymon', 23, ['bartender', 'sniper'])
print(adam.name)
print(adam[0])
print(*adam) # rozpakowanie tupli - unpacking tuple
# named tuples daja nam mozliwosc dostania sie do wartosci zarowno poprzez przesuniecie jak i klucz
# konwersja namedtuple na slownik
D1 = adam._asdict()
print(D1['jobs'])
# print(D1[0]) # typeerror, bo to juz slownik
