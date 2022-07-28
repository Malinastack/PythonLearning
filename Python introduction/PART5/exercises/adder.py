def adder(*args):
    sum = args[0]
    for i in range(1, len(args)):
        sum += args[i]

    return sum



print(adder(2, 3))
print(adder('hello ', 'john'))
print(adder([1, 2, 3, 4], [2, 3, 4, 5]))
print(adder(2.0, 3.5))


def adder2(**kwargs):
    sth = list(kwargs.values())
    sum = sth[0]
    for v in list(kwargs.values())[1:]:
        sum += v

    return sum


print(adder2(a=2, b=3))







