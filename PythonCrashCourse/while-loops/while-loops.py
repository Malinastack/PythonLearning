
while True:
    add_topping = input('What topping would you like to add to your pizza? ')
    if add_topping != 'quit':
        print('Added {} to your pizza'.format(add_topping))
    else:
        break

while True:
    age = int(input('Please tell us your age: '))
    if age < 3:
        print('Your ticket is free')
        break
    if age >= 3 and age < 12:
        print('Your ticket will cost you 10$')
        break
    if age > 12:
        print('Your ticket will cost you 15$')
        break