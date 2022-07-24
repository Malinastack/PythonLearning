print(open('script2.py').read())

print()

for line in open('script2.py'): # najlepsza opcja otwierania pliku?
    print(line, end='')

print()

f = open('script2.py')
print(next(f))
print(next(f))
print(next(f))
print(next(f))

L = [1, 2, 3]
I = iter(L)
print(next(I))
print(next(I))
print(next(I))

f = open('script2.py')
print(iter(f) is f) # obiekt plikowy sam w sobie jest iteratorem


# iteracje ręczne

L2 = [1, 2, 3]
I2 = iter(L2)

while True:
    try:
        X = next(I2)

    except StopIteration:
        print('\nKoniec')
        break
    print(X ** 2, end=' ')

# iteracja automatyczna

L3 = [1, 2, 3]
for x in L3:
    print(x**3, end=' ')
print()
print(sorted(open('script2.py')))
print(list(map(str.upper, open('script2.py'))))
print(list(enumerate(open('script2.py'))))
print(list(zip(open('script2.py'), open('script2.py'))))
print('################################################')
for i in zip(open('script2.py'), open('script2.py')):
    print(i)


L4 = [1, 2, 3, 4] # obiekt iterowalny (iterable)
I = iter(L4) # obiekt iteratora (iterator)
print(next(I)) # obiekt iteratora wygenerowal wartosc
