print('###############ZADANIE1#################')
print(2**16)
print(2/5)
print(2/5.0)
print('mielonka' + 'jajka')
S = 'szynka'
print('jajka' + S)
S2 = S * 5
print(S2)

print(S[:0])# pobiera elementy do 0
S3 = list(S)
S3[:0] = 'siema'
print(S3)
S4 = ''.join(S3)
print(S4)

print("zielone %s i %s" % ('jajka', S))
print('zielone {0} i {1}'.format('jajka', S))
print(('x',)[0])
print(('x', 'y')[1])

L = [1, 2, 3] + [4, 5, 6]
print(f'L: {L}\nL[:]: {L[:]}\nL[:0]: {L[:0]}\nL[-2]: {L[-2]}\nL[-2:]: {L[-2:]}')
print(([1, 2, 3] + [4, 5, 6])[2:4])
L.reverse()
print(L)
L.sort()
print(L)
print(L.index(4))

D = {'x': 1, 'y': 2, 'z': 3}
D['w'] = 0
print(D['x'] + D['w'])
D[(1,2,3)] = 4
print(D)
print(list(D.keys()), list(D.values()), (1,2,3) in D)
print('###############ZADANIE2#################')
L = [0, 1, 2, 3]
# print(L[4]) out of range
print(L[-1000:100]) # po prostu wyprintuje liste
L[2:0] = [4,5,6,7] # skaluje do pustego wycinka np 2:2
print(L)
print('###############ZADANIE3#################')
L = [1, 2, 3, 4]
L[2] = []
print(L)
L[2:3] = []
print(L)
del L[1:]
print(L)
L = [1, 2, 3, 4]
# L[1:2] = 1 błąd
print(L)
print('###############ZADANIE4#################')
X = 'mielonka'
Y = 'jajka'
X, Y = Y, X
print(X, Y)
print('###############ZADANIE5#################')
D = {}
D[1] = 'a'
D[2] = 'b'
D[(1, 2, 3)] = 'c'
print(D)
print('###############ZADANIE6#################')
D = {'a': 1, 'b': 2, 'c':3}
# print(D['d']) # blad brak klucza
D['d'] = 'mielonka'
print(D)
print('###############ZADANIE7#################')
#tekstowe
print('###############ZADANIE8#################')
S = 'jajo'
print(S[0][0][0][0][0])
print('###############ZADANIE9#################')
S = 'jajo'
S = S[:3] + 'a'
print(S)
print('###############ZADANIE10#################')
D1 = dict(dane=dict(imie='Szymon', nazwisko='Malinowski'), wiek=23, zawod=['murarz', 'tynkarz'],
          adres='Olsztyn', email='jakis@mail.pl')
print(D1['dane']['imie'])
print(D1['dane']['nazwisko'])
for i in D1['zawod']:
    print(f'Zawód: {i}')
print('###############ZADANIE11#################')

plik = open('myfile.txt', 'w')

plik.write('Hello world!')

plik = open('myfile.txt', 'r')

print(plik.readline())
