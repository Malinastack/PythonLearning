class SharedData:
    spam = 42


x = SharedData()
y = SharedData()

print(x.spam, y.spam, SharedData.spam)
SharedData.spam = 99
print(x.spam, y.spam, SharedData.spam)
x.spam = 22
print(x.spam, y.spam, SharedData.spam)
SharedData.spam = 115
print(x.spam, y.spam, SharedData.spam)


class MixedNames:
    data = 'mielonka' # zmienne współdzielone

    def __init__(self, value):
        self.data = value # zmienne tylko dla danej instancji

    def display(self):
        print(self.data, MixedNames.data)

    def change(self, sth):
        self.data = sth


class MixedNamesv2(MixedNames):
    pass


x = MixedNames(1)
y = MixedNames(2)
z = MixedNamesv2(3)
x.display()
y.display()
z.display()
x.change('something')
x.display()
y.display()
z.display()
MixedNames.data = 'helllllooooo'
x.display()
y.display()
z.display()