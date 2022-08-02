from classes_introductionv2 import FirstClass


class SecondClass(FirstClass):
    def display(self):
        print(f'Aktualna wartość = {self.data}')


class ThirdClass(SecondClass):
    def __init__(self, value):
        self.data = value

    def __add__(self, other):
        return ThirdClass(self.data + other)

    def __str__(self):
        return '[Third class: %s]' % self.data

    def mul(self, other):
        self.data *= other


x = FirstClass()
z = SecondClass()
z.set_data('Hello')
z.display()
x.set_data('John')
x.display()
a = ThirdClass('abc')
a.display()
print(a)
b = a + 'xyz'
b.display()
a.mul(3)
print(a)
