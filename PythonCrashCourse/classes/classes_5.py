class User:
    def __init__(self, first_name, last_name, age, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.login_attempts = 0

    def describe_user(self):
        print(f'User info:\n'
              f'First name: {self.first_name}\n'
              f'Last name: {self.last_name}\n'
              f'Age: {self.age}\n'
              f'Sex: {self.sex}\n')

    def greet_user(self):
        if self.sex == 'female':
            print(f'Hello Madaam {self.first_name} {self.last_name}')
        else:
            print(f'Hello Sir {self.first_name} {self.last_name}')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Privileges:
    def __init__(self):
        self.privileges = ['can delete post', 'can add post', 'can ban user']

    def show_privileges(self):
        print('This is the list of admin privileges: ')
        for i in self.privileges:
            print(f'- {i}')


class Admin(User):
    def __init__(self, first_name, last_name, age, sex):
        super().__init__(first_name, last_name, age, sex)
        self.privileges = Privileges()




admin = Admin('Janusz', 'Pempek', 48, 'male')
admin.privileges.show_privileges()
