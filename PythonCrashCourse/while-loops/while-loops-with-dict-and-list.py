pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

responses = {}

polling_active = True

# while polling_active:
#     name = input('What is your name? ')
#     response = input('Which mountaint would you like to climb someday')
#
#     responses[name] = response
#
#     repeat = input('Next person? (yes/no) ')
#     if repeat == 'no':
#         polling_active = False
#
#
# for name, response in responses.items():
#     print(f"{name} would like to climb {response}.")
#
# print(responses)

sandwich_orders = ['pastrami', 'ham-cheese', 'pastrami', 'cheese', 'pastrami', 'ham-tomato']
done = []
print('Restaurant run off pastrami sandwiches')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    done_sandwich = sandwich_orders.pop(0)
    print('I made you {} sandwich'.format(done_sandwich))
    done.append(done_sandwich)

print('Done sandwiches: ')
for sandwich in done:
    print(sandwich)

responses = {}
while True:
    name = input('Tell me your name: ')
    response = input('What place in the world would you like to visit? ')
    responses[name] = response

    again = input('Would you like to let another person to make the poll? ')

    if again == 'no':
        break


for k, v in responses.items():
    print(f'{k} answers was {v}')

#wersja z dictionary in dictionary
while True:
    name = input('Tell me your name: ')
    response = input('What place in the world would you like to visit? ')
    response2 = input('How much money you have to spent on vacation? ')
    responses[name] = {'money': response2, 'place': response}

    again = input('Would you like to let another person to make the poll? ')

    if again == 'no':
        break


for k, v in responses.items():
    print(f'{k} answers was {v}')

