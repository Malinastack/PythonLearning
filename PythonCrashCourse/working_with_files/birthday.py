with open('million_digits.txt') as file_object:
    lines2 = file_object.readlines()

long_pi_string = ''

birthday = input('Enter your birthday in the form mmddyy: ')

for line in lines2:
    long_pi_string+=line.strip()

if birthday in long_pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")