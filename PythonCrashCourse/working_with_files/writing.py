filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

filename2 = 'guests.txt'
guest_name = input('tell us your name: ')
with open(filename2, 'a') as file_object:
    file_object.write(guest_name)

filename3 = 'guest_book.txt'
with open(filename3, 'a') as file_object:
    while True:
        guest_name2 = input('tell us your name: ')
        file_object.write(f'{guest_name2}\n')
        con = input('Do you want to continue? (yes/no)')
        if con == 'no':
            break

