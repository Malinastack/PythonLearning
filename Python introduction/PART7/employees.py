class Employee:
    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary

    def give_raise(self, percent):
        self.salary = self.salary + self.salary*(percent/100)

    def work(self):
        print(self.name, 'do his/her job')

    def __repr__(self):
        return f'Pracownik:{self.name}\nwynagrodzenie:{self.salary}'


class Chef(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, salary=50000)

    def work(self):
        print(self.name, 'preparing food')


class Server(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, salary=40000)

    def work(self):
        print(self.name, 'supports the client')


class PizzaRobot(Chef):
    def __init__(self, name):
        Chef.__init__(self, name)

    def work(self):
        print(self.name, 'preparing pizza')

if __name__ == '__main__':
    bob = PizzaRobot('Roberto')
    print(bob)
    bob.work()
    bob.give_raise(20)
    print(bob)
    print()

    for sth in Employee, Chef, Server, PizzaRobot:
        obj = sth(sth.__name__)
        obj.work()