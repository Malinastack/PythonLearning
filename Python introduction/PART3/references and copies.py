X = [1, 2, 3]
L = ['a', X, 'b']
D = {'x': X, 'y': 2}
X[1] = 'suprise'
print(L)
print(D)
X = [1, 2, 3]
L = ['a', X[:], 'b'] # tutaj bezposrednio wstawiamy kopie dlatego ponizsze x[1] = 'suprise'
D = {'x': X[:], 'y': 2} # nie ma wplywu na te liste czy slownik
X[1] = 'suprise'
print(L)
print(D)
X = [1, 2, 3]
L = ['a', X, 'b']
D = {'x': X, 'y': 2}
A = L[:]
B = D.copy()
A[1] = 'ni'
B['c'] = 'mielonka'
print('Kopia L i zmieniono na 1 indeksie na "ni"')
print(A)
print('Oryginal')
print(L)
print('Kopia D i dodano c: "mielonka"')
print(B)
print('Oryginal')
print(D)

L1 = [1, ('a', 3)]
L2 = [1, ('a', 3)]

print(L1 == L2, L1 is L2) # True, False


S1 = 'test'
S2 = 'test'

print(S1 == S2, S1 is S2) # True, True

S3 = 'much more longer string'
S4 = 'much more longer string'
S5 = 'much more longer than expected string'
S6 = 'much more longer than expected string'
print(S5 == S6, S5 is S6) # True, True
# python wewnętrznie umieszcza łanuchy znaków w pamięci podręcznej i ponownie ich używa zze względu na optymalizacje

print(str(11) >= '11', 11 >= int('11'))  # True, True

