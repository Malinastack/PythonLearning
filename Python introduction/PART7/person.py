from classtools import AttrDisplay


class Person(AttrDisplay):
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastname(self):
        return self.name.split()[-1]

    def give_raise(self, percent):
        self.pay = int(self.pay * (1 + (percent/100)))


class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'manager', pay)

    def give_raise(self, percent, bonus=10):
        Person.give_raise(self, percent+bonus)


if __name__ == '__main__':
    bob = Person('Bob')
    anna = Person('Anna', job='developer', pay=10000)
    Tom = Manager('Tom Black', pay=20000)
    print(bob.name, bob.pay)
    print(anna.name, anna.pay)
    print(f'{anna.name} zarabia: {anna.pay}')
    anna.pay*=1.15
    print(f'{anna.name} zarabia: {anna.pay}')
    anna.give_raise(15)
    print(f'{anna.name} zarabia: {anna.pay}') # better 
    print(f'{Tom.name} zarabia: {Tom.pay}')  # better
    Tom.give_raise(10)
    print(f'{Tom.name} zarabia: {Tom.pay}')  # better
    print(Tom.lastname())
    print(Tom.job)
    print(Tom.__class__.__name__)
    print(Tom.__class__)
    print(anna)
    print(bob)
    print(Tom)

