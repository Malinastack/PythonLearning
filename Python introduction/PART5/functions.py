def intersect(seq1, seq2):
    seq3 = [x for x in seq1 if x in seq2]
    return seq3


print(intersect([1, 2, 3, 4], [2, 5, 4, 7]))

list = [1, 2, 3, 4, 5]
print([x for x in list.__dir__() if not x.startswith('__')])

X = 88

def func():
    # global X
    # jesli uzyjemy global, zmienimy globalna zmienna X,
    # bez tego, X wewnatrz funkcji jest tylko zmienna lokalna
    X = 99

func()
print(X)

Y = 99


def f1():
    Y = 88


    def f2():
        print(Y)
    # f2()
    return f2


# f1() # wyświetla 88 - zmienna lokalną funkcji zawierającej
action = f1()
action() # wyświetla 88


def maker(n):
    def dosomething(x):
        return x**n
    return dosomething


f = maker(2)
print(f)
print(f(3)) # wywolujemy zagniezdzona funkcje ktora zostala utworzona i zwrocona przez funkcje maker


def maker2(n):
    return lambda x: x**n


g = maker(3)
print(g(5))


def f1():
    x = 88
    f2(x)


def f2(x):
    print(x) # plaska struktura lepsza niz zagniezdzona


f1()

def func():
    x = 4
    action = (lambda n: x ** n)
    return action

x = func()
print(x(2))


def make_actions():
    acts = []
    for i in range(5):
        acts.append(lambda x: i ** x)
    return acts


sth = make_actions()
print(sth[0])
print(sth[0](2))
print(sth[1](2))
print(sth[2](2))
print(sth[3](2)) # wszystkie sa takie same poniewaz funkcja zagnieżdzona (lambda) zapamietala te sąmą ostatnią wartość i


def make_actions2():
    acts = []
    for i in range(5):                      # użycie domyślnych wartosci argumentow
        acts.append(lambda x, i=i: i ** x)  # zapamietanie biezacej wartosci i
    return acts


sth2 = make_actions2()
print(sth2[0])
print(sth2[0](2))
print(sth2[1](2))
print(sth2[2](2))
print(sth2[3](2))