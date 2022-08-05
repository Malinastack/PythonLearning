class Squares:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        for value in range(self.start, self.stop + 1):
            yield value ** 2


for i in Squares(1, 5):
    print(i, end=' ')
print()
S = Squares(1, 3)
for i in S:
    for j in S:
        print(f'({i}, {j})')