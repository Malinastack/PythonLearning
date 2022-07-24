class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'Restaurant name is {self.restaurant_name} '
              f'and the type of cuisine is {self.cuisine_type}.')

    def open_restaurant(self):
        print(f'Restaurant {self.restaurant_name} is open!')


restaurant = Restaurant('Adiosa', 'Turkey')
restaurant2 = Restaurant('Amigos', 'Chinese')
restaurant3 = Restaurant('DosLabos', 'Mexico')
restaurant.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

restaurant.open_restaurant()


class User:
    def __init__(self, first_name, last_name, age, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex

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


user1 = User('Thomas', 'Smith', 52, 'male')
user2 = User('Jessica', 'Smith', 12, 'female')
user3 = User('Catrine', 'Swiss', 24, 'female')

user1.describe_user()
user1.greet_user()
print('\n')
user2.describe_user()
user2.greet_user()
print('\n')
user3.describe_user()
user3.greet_user()
print('\n')
