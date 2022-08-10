from employees import PizzaRobot, Server


class Customer:
    def __init__(self, name):
        self.name = name

    def order(self, server):
        print(self.name, 'order from', server.name)

    def pay(self, server):
        print(self.name, 'paying for order')


class Oven:
    def bake(self):
        print('oven baking')


class PizzaShop:
    def __init__(self):
        self.server = Server('Adam')
        self.chef = PizzaRobot('Roberto')
        self.oven = Oven()

    def order(self, name):
        customer = Customer(name)
        customer.order(self.server)
        self.chef.work()
        self.oven.bake()
        customer.pay(self.server)


if __name__ == '__main__':
    scene = PizzaShop()
    scene.order('Customer1')
    print('...')
    scene.order('Customer2')
