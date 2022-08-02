class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastname(self):
        return self.name.split()[-1]

    def give_raise(self, percent):
        self.pay = int(self.pay * (1 + (percent/100)))


if __name__ == '__main__':
    bob = Person('Adam')
    anna = Person('Elise', job='developer', pay=10000)
    print(bob.name, bob.pay)
    print(anna.name, anna.pay)
    print(f'{anna.name} zarabia: {anna.pay}')
    anna.pay*=1.15
    print(f'{anna.name} zarabia: {anna.pay}')
    anna.give_raise(15)
    print(f'{anna.name} zarabia: {anna.pay}') # better
