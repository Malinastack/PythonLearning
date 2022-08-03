from person import Person, Manager


class Department:
    def __init__(self, *args):
        self.members = list(args)

    def add_member(self, person):
        self.members.append(person)

    def give_raises(self, percent):
        for person in self.members:
            person.give_raise(percent)

    def show_all(self):
        for person in self.members:
            print(person)


if __name__ == '__main__':
    bob = Person('Robert Lewandowski')
    sue = Person('Anna Miss', job='dev', pay=5600)
    tom = Manager('Tomas Black', pay=8000)

    development = Department(bob, sue)
    development.add_member(tom)
    development.give_raises(10)
    development.show_all()
    print(bob.__class__.__name__)
    print(bob.__class__)
    print(sue.__class__.__name__)
    print(sue.__class__)
    print(tom.__class__.__name__)
    print(tom.__class__)