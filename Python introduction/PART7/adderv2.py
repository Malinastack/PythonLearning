class Adderv2:
    def __init__(self, value):
        self.data = value

    def __add__(self, other):
        print('add', self.data, other)
        return self.data + other

    def __radd__(self, other):
        print('radd', self.data, other)
        return other + self.data


x = Adderv2(88)
y = Adderv2(99)
print(x + 1)
print(1 + y)
