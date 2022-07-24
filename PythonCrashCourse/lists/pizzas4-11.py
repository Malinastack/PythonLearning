my_pizzas = ['margharita', 'capriciosa', 'salami', 'pepperoni']

your_pizzas = my_pizzas[:]

my_pizzas.append('brocolli')
your_pizzas.append('cheetos')

print(my_pizzas)
print(your_pizzas)

for i in my_pizzas:
    print(i)
print('\n')
for i in your_pizzas:
    print(i)
