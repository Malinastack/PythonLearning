class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastname(self):
        return self.name.split()[-1]

    def give_raise(self, percent):
        self.pay = int(self.pay * (1 + (percent/100)))

    def __repr__(self):
        return f'Person: {self.name}\nSalary: {self.pay}'


class Manager:
    def __init__(self, name, pay):
        self.person = Person(name, 'manager', pay)

    def give_raise(self, percent, bonus=10):
        Person.give_raise(self, percent+bonus)