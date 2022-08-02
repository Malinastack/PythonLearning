class Employee:
    def __init__(self):
        self.salary = 5000

    def computesalary(self):
        print(self.salary)

    def giveraise(self):
        ...

    def promote(self):
        ...

    def retire(self):
        ...


class Engineer(Employee):
    def __init__(self):
        self.salary = 8000

    def computesalary(self):
        print(self.salary)


Szymon = Engineer()
Szymon.computesalary()
Agata = Employee()
Agata.computesalary()