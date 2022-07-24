with open('pi_digits.txt') as file_object:
    # contents = file_object.read()
    lines = file_object.readlines()

# print(contents)
pi_string = ''
for line in lines:
    pi_string+=line.strip()
print(pi_string)



