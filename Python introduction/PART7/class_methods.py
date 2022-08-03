class NextClass:
    def __init__(self):
        self.message = None

    def printer(self, text):
        self.message = text
        print(self.message)


x = NextClass()
x.printer('wywołanie instancji') # wywolanie metody instancji
print(x.message) # bezposrednie wyswietlenie atrybutu instancji

# mozna jeszcze tak

NextClass.printer(x, 'wywolanie klasy') # bezpośrednie wywołanie klasy
print(x.message)

# wywolywanie konstruktorów klas nadrzędnych


class Test:
    def __init__(self, x):
        self.x = x + 1

    def do_something(self):
        self.x = 10


class Testv2(Test):
    def __init__(self, x, y):
        Test.__init__(self, x)
        self.y = y

    def __repr__(self):
        return f'{self.x}, {self.y}'

    def do_something(self):
        super().do_something()
        self.x += 2


something = Testv2(1, 2)
print(something)
something.do_something()
print(something)