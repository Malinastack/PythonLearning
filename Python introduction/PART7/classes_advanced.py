class Super:
    def hello(self):
        self.data1 = 'something'


class Sub(Super):
    def hola(self):
        self.data2 = 'great'


X = Sub()
print(X.__dict__)
X.hello()
print(X.__dict__)
X.hola()
print(X.__dict__)

X.data3 = 'tost'
print(X.data3)
print(X.__dict__)