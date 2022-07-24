L1 = [1, 2, 3, 4]
L2 = [5, 6, 7, 8]
# zip buduje liste krotek
print(list(zip(L1, L2)))

for (x, y) in zip(L1, L2):
    print(x, y, '--', x+y)

T1, T2, T3 = [1, 2, 3], [4, 5, 6], [7, 8, 9]

print(list(zip(T1, T2, T3))) # trzy krotki dla trzech argumentow

S1 = 'abc'
S2= 'xyz123'

print(list(zip(S1, S2))) # odcina krotki do długości najkrótszego elementu
print(list(map(ord, S2))) # zwraca liste

keys = ['mielonka', 'jajka', 'tost']
vals = [1, 3, 5]

D = {}
for (k, v) in zip(keys, vals):
    D[k] = v

print(D)

# lepsza wersja ^
D2 = dict(zip(keys, vals))
print(D2)

# enumerate

S = 'mielonka'
for(offset, item) in enumerate(S):
    print(item, 'wystepuje na pozycji', offset)
# enumerate zwraca obiekt generatora
E = enumerate(S)
print(next(E))
print(next(E))
print(next(E))
print(next(E))
print(next(E))


M = map(abs, (-1, 0, 1))
print(M)
print(next(M))
print(next(M))
print(next(M)) # reczne uzycie iteratora "zuzywa" wyniki


print('Punkt1')

for x in M:
    print(x)

M = map(abs, (-1, 0, 1))

print('Punkt2')

for x in M:
    print(x)

print('Punkt3')

print(list(map(abs, (-1, 0, 1))))

M = map(abs, (-1, 0, 1))

for x in M:
    print(x)

