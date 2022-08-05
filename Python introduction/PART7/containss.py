class Iters:
    def __init__(self, value):
        self.data = value

    def __getitem__(self, i): # metoda zastepcza do uzcia przez iteracje oraz do indeksowania i wycinania
        print('get[%s]:' % i, end='')
        return self.data[i]

    def __iter__(self): # metoda preferowana w iteracji, pozwala na uzycie tylko jednego iteratora
        print('iter=> next:', end='')
        for x in self.data:
            yield x
            print('next:', end='')

    def __contains__(self, x): # metoda preferowana w operacji in
        print('contains: ', end='')
        return x in self.data



x = Iters([1, 2, 3, 4, 5])
print(3 in x)


for i in x:
    print(i, end=' | ')

print()
print([i ** 2 for i in x])
print(list(map(bin, x)))

i = iter(x)

while True:
    try:
        print(next(i), end=' @ ')
    except StopIteration:
        break

print()
x = Iters('spam')
print(x[0])
print(x[1:])
print(list(x))