def f(a):
    a = 99 # modyfikacja tylko zmiennej lokalnej a

b = 88
f(b)
print(b) # 88

def changer(a, b):
    a = 2
    b[0] = 'something'

X = 1
L = [1, 2]
changer(X, L) # X bez zmian, natomiast w L zmiana ponieważ L jest obiektem mutowalnym
print((X, L))
# to tak samo jak

X = 1
a = X
a = 2
print(X) # 1 bo a jest obiektem niemutowalnym
L = [1, 2]
b = L
b[0] = 10
print(L) # [10, 2] bo L jest obiektem mutowalnym

# aby uniknąc zmian obiektu mutowalnego przekazanego do funkcji mozna
changer(X, L[:])
print(L)
# lub
changer(X, L.copy())
print(L)
# lub


def changer(a, b):
    b = b[:]
    a = 2
    b[0] = 'mielonka'

changer(X, L)
print(L)


def multiple(x, y):
    x = 2
    y = [3, 4]
    return x, y

X = 1
L = [1, 2]
X, L = multiple(X, L)
print(X, L)


def f(a, b, c):
    print(a, b ,c)

f(1, 2, 3)

def f(a, b=2, c=3):
    print(a, b, c)

f(1)
f(1, 4)

print('####ARGS####')


def f(*args):
    print(args)

f()
f(1, 2, 3, 4, 5, 6)

print('####KWARGS####')


def f2(**kwargs):
    print(kwargs)

f2()
f2(a=1, b=2)

print('####ARGS+KWARGS####')


def f3(x, *args, **kwargs):
    print(x, args, kwargs)


f3(1, 2, 3, a=2, b=3, c=4)

print('####unpacking arguments####')


def func(a, b, c, d):
    print(a, b, c, d)


args = (1, 2, 3, 4)
func(*args)

D = {'a': 2, 'b':3, 'c': 4 }
D['d'] = 1
func(**D)

if 1 == True:
    action, args = f3, (1, 2, 3, 4, 5)
else:
    action, args = f3, (1,)

action(*args)


def tracer(func, *args, **kwargs):
    print('Wywolanie:', func.__name__)
    return func(*args, **kwargs)


def func(x, y, c, d):
    return x + y + c + d


print(tracer(func, 1, 2, c=3, d=4))


# keyword only argument
print('####key-word_only_arguments####')
def kwonly(a, *b, c):  # kolejnosc (pozycyjne, klucz=wartosc, args, kwargs)
    print(a, b, c)


# kwonly(1, 2, 3)  # blad: missing 1 required keyword-only argument: 'c'

kwonly(1, 2, c=10)  # 1 (2,) 10
kwonly(1, c=3)  # 1 () 3


def kwonly2(x, *, y='hello', c='John'):
    print(x, y, c)


kwonly2(1, y=2, c=3) # 1 2 3
# kwonly2(1, 2) # blad: takes 1 positional argument but 2 were given
kwonly2(1) # 1 hello John


def kwonly3(x, *, y='hello', z, w='John'):
    print(x, y, z, w)


# kwonly3(1) # blad missing 1 required keyword-only argument: 'z'
kwonly3(1, z=3) # 1 hello 3 John
kwonly3(1, y=3, z=3, w=3) # 1 3 3 3


def f(a, c=6, *b, **d):
    print(a, b, c, d)


f(1, 2, 3, 4, 5, g=2, f=5) # c nie jest argumentem będacym slowem kluczowym


def f(a, *b, c=6, **d):
    print(a, b, c, d)


f(1, 2, 3, 4, 5, g=2, f=5) # c juz jest argumentem będacym slowem kluczowym 1 (2, 3, 4, 5) 6 {'g': 2, 'f': 5}
f(1, 2, 3, 4, 5, c=8, g=2, f=5) # nadpisanie wartosci domyslnej c           1 (2, 3, 4, 5) 8 {'g': 2, 'f': 5}


def f(a, *b, c=6, **d):
    print(a, b, c, d)


f(1, *(2, 3), **dict(x=4, y=5, c=7)) # c rowniez zostalo nadpisane
# to samo co
f(1, *(2,3), c=7, **dict(x=4, y=5))
# i to samo co
f(1, c=7, *(2,3), **dict(x=4, y=5))


def minimum(*sth):
    start = sth[0]
    for i in sth:
        if i < start:
            start = i
    return start


print(min(1, 2, 3, 4, -5, 6, 6, 6, 2, 3, 4))


def minmax(test, *sth2):
    start = sth2[0]
    for i in sth2:
        if test(i, start):
            start = i
    return start


def less_than(x, y):
    return x < y


def greater_than(x, y):
    return x > y


print(minmax(greater_than, 4, 2, 3, 4, 5, 6, 7))
print(minmax(less_than, 4, 2, 3, 4, 5, 6, 7))