def echo(message):
    print(message)

x = echo
x('Siemka') # wywolanie posrednie


def indirect(func, arg):
    func(arg)

indirect(echo, 'Wywolanie argumentu ')


def lower_than(x):
    return x < 10

def test(x):
    if lower_than(x):
        print('x is lower than 10')
    else:
        print("x isn't lower than 10")


test(9)


schedule = [(echo, 'Something'), (echo, 'Else')]

for (func, arg) in schedule:
    func(arg)