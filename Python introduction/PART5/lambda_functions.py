import sys

from tkinter import *

def func(x, y, z):
    return x + y + z


print(func(1, 2, 3))


f = lambda x, y, z: x + y + z
print(f(1, 2, 3))

x = lambda a='first', b='second', c='third': a + b + c # wartosci domyslne dzialaja tak samo jak w zwyklych funkcjach
print(x('last'))


def knights():
    title = 'Sir'
    action = (lambda y: title + ' ' + y)

    return action


t = knights()
print(t('Robin'))

key = 'już'
D = {'mam': (lambda: 2 + 2),
     'już': (lambda: 2 * 4),
     'jeden': (lambda: 2**6)}

print(D[key]())  # nawiasy wymuszaja wywolanie funkcji lambda
print(D[key])  # <function <lambda> at 0x7fbd064693a0>

showall = (lambda z: [print(word) for word in z])
t = showall(['hello', 'john', 'doe'])

print()

showall2 = (lambda z: print(*z))
t = showall2(['hello', 'john', 'doe'])

print()

def unpack(items):
    for v in items:
        for i in v:
            print(i)

print()

showall3 = (lambda *w, **z: (unpack(z.values()), print(sum(w))))
t = showall3(1, 2, 3, 4, 5, lista=['hello', 'john', 'doe'])


def action(x):
    return lambda y: x + y


act = action(12)
print(act(2))


action2 = (lambda x: (lambda y: x + y))
act = action2(50)
print(act(10))
print()
print((lambda x: (lambda y: x + y))(15)(5))

x = Button(
    text='Click me',
    command=(lambda: print('Something'))
)
x.pack()
mainloop()