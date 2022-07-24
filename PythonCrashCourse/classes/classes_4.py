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


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavours):
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = flavours

    def display_flavours(self):
        print('There are these flavours available: ')
        for i in self.flavours:
            print(f'- {i}')


icecreamrestaurant = IceCreamStand('Lodziki', 'Lodowa', ['vanilla', 'strawberry', 'blueberry'])
icecreamrestaurant.display_flavours()