T = [(1, 2), (3, 4), (5, 6)]
for (a, b) in T:
    print(a, b)

D = dict(a=1, b=2, c=3)

for key, value in D.items():
    print(key, ' = ', value)

for ((a, b), c) in [((1, 2), 3), ((4, 5), 6), ('XY', 7)]: # przypisanie jest uniwersalne
    print(a, b, c)

print('Z użyciem wycinka')
for i in [(1, 2, 3 ,4 ), (5, 6, 7, 8)]:
    a, b, c = i[0], i[1:3], i[3]
    print(a, b, c)
print('Wycinki zwracają zawsze typ z którego jest wycinane')

print('Z użyciem *')
for a, *b, c in [(1, 2, 3 ,4 ), (5, 6, 7, 8)]:
    print(a, b, c)
print('* zawsze zwraca liste')


items = ['aaa', 111, (4, 5), 2.01]
tests = [(4, 5), 3.14]

for key in tests:
    for item in items:
        print(key, 'znaleziono')
        break
    else:
        print(key, 'nie znaleziono')

for key in tests:
    if key in items:
        print(key, 'znaleziono')
    else:
        print(key, 'nie znaleziono')


seq1 = 'biedronka'
seq2 = 'mielonka'

print([x for x in seq1 if x in seq2])


# wbudowana funkcja range

print(list(range(-5, 5)))
print(list(range(5, -5, -1)))

for i in range(len(seq1)):
    print(seq1[i], end=' ')

print()

S = 'mielonka'

for i in range(len(S)):
    S = S[1:] + S[:1]
    print(S, end=' ')

print()

S = 'mielonka'
for i in range(len(S)):
    X = S[i:] + S[:i]
    print(f'S[{i}:]: {S[i:]} S[:{i}]: {S[:i]}')
    print(X)

S = 'abcdefghijk'

for i in range(0, len(S), 2):
    print(S[i], end=' ')

print()

for i in S[::2]: # wycinek z co drugiego elementu
    print(i, end=' ')

print()

L = [1, 2, 3, 4, 5]
for i in range(len(L)):
    L[i] += 1

print(L)

print([x+1 for x in L])

