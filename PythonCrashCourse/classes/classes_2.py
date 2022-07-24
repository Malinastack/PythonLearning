class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f'Restaurant name is {self.restaurant_name} '
              f'and the type of cuisine is {self.cuisine_type}.')

    def open_restaurant(self):
        print(f'Restaurant {self.restaurant_name} is open!')

    def set_number_served(self, number):
        self.number_served = number
        print(f'Today served number of customers: {self.number_served}')

    def increment_number_served(self, number):
        self.number_served += number
        print(f'Today served number of customers: {self.number_served}')


restaurant1 = Restaurant('LosBados', 'Mexico')
restaurant1.set_number_served(10)
print('Adding serve')
restaurant1.increment_number_served(15)


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


user1 = User('Thomas', 'Smith', 52, 'male')
print(user1.login_attempts)
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)
