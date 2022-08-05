class Adder:
    def __init__(self, value=0):
        self.data = value

    def __add__(self, other):
        self.data += other


class Addrepr(Adder):
    def __repr__(self):
        return f'addrepr {self.data}'


x = Addrepr(2)
x + 1
print(x)