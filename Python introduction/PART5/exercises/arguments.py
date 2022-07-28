def f1(a, *b, c):
    print(a, b, c)


f1(1, 2, 3, 4, c=5)


def f2(a, b, *c):
    print(a, b, c)


f2(1, 2, 3, 4, 5)


def f3(a, *b, **c):
    print(a, b, c)


f3(1, 2, 3, 4, 5, x=1, b=2, c=3)

