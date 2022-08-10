class Life:
    def __init__(self, name='nieznajomy'):
        print('Witaj', name)
        self.name = name

    def __del__(self):
        print('Żegnaj', self.name)


brian = Life('Brian')


class Test:
    def __init__(self, start, stop):
        self.value = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2


class Test2:
    def __init__(self, start, stop):
        self.value = start
        self.stop = stop

    def __iter__(self):
        for i in range(self.value, self.stop+1):
            yield i ** 2



x = Test(1, 10)

for i in x:
    print(i, end=' ')
print()
x = Test2(1, 10)
for i in x:
    print(i, end=' ')