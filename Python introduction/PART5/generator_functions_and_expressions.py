import math

def gensquares(n):
    for i in range(n):
        yield i ** 2


gen1 = gensquares(5)
print(next(gen1))
print(next(gen1))
print(next(gen1))

lista = [1, 2, 3, 4]
sth = map((lambda x: x + 10), lista) # tak jak generator map jest swoim iteratorem
print(next(sth))


def gen():
    for i in range(10):
        x = yield i
        print(x)


G = gen()
print(next(G))
G.send(77)
print(next(G))
print(next(G))
G.send(88)
print(next(G))
print(next(G))

print([x ** 2 for x in range(4)])  # [0, 1, 4, 9]
G2 = (x ** 2 for x in range(4))  # <generator object <genexpr> at 0x7f7490dd1890>

print(iter(G2) is G2)  # True

print(next(G2))
print(next(G2))
print(next(G2))
print(next(G2))

print(''.join(x.upper() for x in 'aaa,bbb,ccc'.split(',')))

print(sorted((x ** 2 for x in range(4)), reverse=True))


G3 = map(math.sqrt, (x ** 2 for x in range(5)))
print(iter(G3) is G3)
print(next(G3))
print(next(G3))

line = 'aa bbb c'
try:
    G4 = (filter(lambda x: len(x) > 1, line.split()))
    print(next(G4))
    print(next(G4))
    print(next(G4))
except StopIteration:
    print('The end')

#  a teraz to samo bez uzycia filter

G5 = (x for x in line.split() if len(x) > 1)
print(next(G5))
print(next(G5))


#  umieszczenie list przed generatorem wymusza podanie wszystkich wynikow

G6 = (x ** 3 for x in range(12) if x % 2 == 0)
print(list(G6)) # [0, 8, 64, 216, 512, 1000]

# generator obsługuje tylko jedną aktywną iteracje

G7 = (x ** 3 for x in range(12) if x % 2 == 0)

I1 = iter(G7)
I2 = iter(G7)

print(next(I1))  # 0
print(next(I1))  # 8
print(next(I2))  # 64
print(next(I2))  # 216
print(next(I1))  # 512

#  a listy juz wiecej :)

L = [1, 2, 3, 4, 5]
I1, I2 = iter(L), iter(L)

print(next(I1))
print(next(I1))
print(next(I2))
print(next(I2))
print(next(I1))

# FROM GENERATOR delegowanie dzialania do subgeneratora

# przyklad bez from generator
def both(n):
    for i in range(n):
        yield i
    for i in (x **2 for x in range(n)):
        yield i


print(list(both(5)))


def both2(n):
    yield from range(n)
    yield from (x ** 2 for x in range(n))


print(list(both2(5)))

# generowanie mieszanych sekwencji


L, S = [1, 2, 3], 'spam'
for i in range(len(S)):
    S = S[1:] + S[:1]
    print(S, end=' ')


def scramble(seq):
    res = []
    for i in range(len(seq)):
        seq = seq[1:] + seq[:1]
        res.append(seq)
    return res

print(scramble(S))


def scramble_generator(seq):
    for i in range(len(seq)):
        seq = seq[1:] + seq[:1]
        yield seq


gen2 = scramble_generator('something')
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))

print('\nother generator\n')


def scramble_generatorv2(seq):
    for i in range(len(seq)):
        yield seq[i:] + seq[:i]


gen3 = scramble_generatorv2('something')
print(next(gen3))
print(next(gen3))
print(next(gen3))
print(next(gen3))


gen4 = (S[i:] + S[:i] for i in range(len(S)))
print(list(gen4))