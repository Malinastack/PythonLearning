def func(a: 'first', b, c: 'last'):
    return a + b + c

print(func(1, 2, 3))
print(func.__annotations__)