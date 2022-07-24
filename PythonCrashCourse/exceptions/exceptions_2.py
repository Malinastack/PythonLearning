try:
    with open('cats.txt', 'r') as file_object:
        print(file_object.read())
    with open('dog.txt', 'r') as file_object:
        print(file_object.read())
except FileNotFoundError as err:
    # print(f'Jeden z plików nie istnieje')
    pass