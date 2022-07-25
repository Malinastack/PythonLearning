def tester(start):
    state = start

    def nested(label):
        print(label, state)
    return nested

F = tester(0)
F('something')  # something 0
F('something else')  # something else 0


# def tester(start):
#     state = start
#
#     def nested(label):
#         print(label, state)
#         state += 1 # domyślnie nie może sie zmienic
#     return nested

def tester(start):
    state = start # kazde wywolanie otrzymuje wlasna zmienna state

    def nested(label):
        nonlocal state # pamieta state z zasiegu funkcji zawierajacej
        print(label, state)
        state += 1 # mozna zmienic jesli nonlocal
    return nested

F = tester(0)
F('search something')  # something 0
F('search something else')  # something else 1

#kazde wywolanie ma inne informacje o stanie
G = tester(45)
G('checking something')  # checking something 45
G('checking something else')  # checking something else 46
F('search something else again')  # search something else again 2





