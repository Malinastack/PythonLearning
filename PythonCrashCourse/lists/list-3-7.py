list = ['Adam', 'Andrzej', 'Konrad']

print(f"Hey {list[0]}, {list[1]}, {list[2]} I got bigger table")

list.insert(0, 'Patryk')
list.insert(2, 'Tomek')
list.append('Szymon')

print(f'Siema {list[0]}')
print(f'Siema {list[1]}')
print(f'Siema {list[2]}')
print(f'Siema {list[3]}')
print(f'Siema {list[4]}')
print(f'Siema {list[5]}')

print(f"Hey {list[0]}, {list[1]}, {list[2]}, {list[3]}, {list[4]}, {list[5]} I got too small table")

first_removed = list.pop()
second_removed = list.pop()
third_removed = list.pop()
fourth_removed = list.pop()

print(f"sorry {first_removed}")
print(f"sorry {second_removed}")
print(f"sorry {third_removed}")
print(f"sorry {fourth_removed}")

print(f"Hey {list[0]}, {list[1]} you are still invited")

del list[1]
del list[0]
print(list)