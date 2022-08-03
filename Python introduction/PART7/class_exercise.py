class Person:
    def __init__(self, name, lastname, age, pay=0):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.pay = pay

    def change_pay(self, value):
        self.pay = value

    def give_raise(self, percent):
        self.pay = self.pay*(1 + percent/100)

    def __repr__(self):
        return f'Imię: {self.name}\n' \
               f'Nazwisko: {self.lastname}\n' \
               f'Wiek: {self.age}\n' \
               f'Zarobki: {self.pay}'


class Employee(Person):
    def __init__(self, name, lastname, age):
        Person.__init__(self, name, lastname, age, 2000)


class Manager(Person):
    def __init__(self, name, lastname, age):
        Person.__init__(self, name, lastname, age, 5000)

    def give_raise(self, percent, bonus=10):
        Person.give_raise(self, percent+bonus)


class Company:
    def __init__(self, *args):
        self.members = list(args)

    def show_all(self):
        print('#####COMPANY MEMBERS#####')
        for i in self.members:
            print(i, '\n')

    def give_raises(self, percent):
        for i in self.members:
            i.give_raise(percent)


pracownik1 = Employee('Adam', 'Roztocki', 22)
pracownik2 = Employee('Andrzej', 'Malinowski', 25)
manager1 = Manager('Tomasz', 'Super', 34)
print(pracownik1)
print()
print(manager1)
print('\nDajemy podwyżkę 10% pracownikowi\n')
pracownik1.give_raise(10)
print(pracownik1)
print('\nDajemy podwyżkę 10% managerowi\n')
manager1.give_raise(10)
print(manager1)
company1 = Company(pracownik1, pracownik2, manager1)
company1.show_all()
print('\nDajemy wszystkim podwyżki 10%\n')
company1.give_raises(10)
company1.show_all()