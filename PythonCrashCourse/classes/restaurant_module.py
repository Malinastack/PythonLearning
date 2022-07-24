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