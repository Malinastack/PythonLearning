E = enumerate('spam') # tak samo jak plik jest obiektem iterowalnym i iteratorem
print(E)
I = iter(E)
print(next(I))
print(next(I))
print(next(I)) # zwraca tuple (index, wartosc)
print(next(I))
print(list(enumerate('spam'))) # przekształcenie enumerate na liste generuje wszystkie elementy jednoczesnie

E = enumerate('hello')
print(next(E))
print(next(E))
print(next(E))
print(next(E))
print(next(E))

