class FirstClass:

    def set_data(self, value):
        self.data = value

    def display(self):
        print(self.data)

if __name__ == '__main__':
    x = FirstClass()
    y = FirstClass()

    x.set_data(5000)
    x.display()
    x.data = 'Hi'
    x.display()
    x.another_name = 'something'
