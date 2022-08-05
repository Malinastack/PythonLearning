class Number:
    def __init__(self, start):
        self.data = start

    def __sub__(self, other):
        return Number(self.data - other)


class Indexer:
    def __getitem__(self, item):
        return item**2


x = Number(5)
y = x - 2
print(y.data)
x = Indexer()
print(x[2])
for i in range(5):
    print(x[i], end=' ')


class Indexerv2:
    data = [5, 6, 7, 8, 9]

    def __getitem__(self, item):
        print('getitem:', item)
        return self.data[item]



print()
x = Indexerv2()
print(x[0])
print(x[1])
print(x[2])


class StepperIndex:
    def __getitem__(self, i):
        return self.data[i]


x = StepperIndex()
x.data = 'Something'
print(x[1])
for item in x:
    print(item, end=' ')


