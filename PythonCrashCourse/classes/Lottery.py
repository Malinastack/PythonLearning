from random import choice

pick = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Z', 'W', 'X', 'A']
winners = []
for i in range(4):
    win = choice(pick)
    winners.append(win)

print('This numbers/letter wins: ')
for i in winners:
    print(f'- {i}')

my_ticket = []
counter = 0
while True:
    counter += 1
    for i in range(4):
        win = choice(pick)
        my_ticket.append(win)

    if my_ticket == winners:
        print(f'It takes {counter} loops to win')
        print(my_ticket)
        break
    else:
        my_ticket = []



