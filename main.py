name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())
first_name = "Szymon"
last_name = "Malinowski"
full_name = f"{first_name} {last_name}"
print(full_name)
full_name2 = "{} {}".format(first_name, last_name)
print(full_name2)


from PIL import Image

file_in = "PythonCrashCourse/ship2.png"
img = Image.open(file_in)

file_out = "ship2.bmp"
img.save(file_out)

with open('Python introduction/PART3/nowy/tekst.txt') as read_object:
    lines = read_object.readlines()

for line in lines:
    print(line)

