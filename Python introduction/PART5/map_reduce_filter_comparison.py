from functools import reduce

list1 = [1, 2, 3, 8, 9, 10]

def add(x):
    return x + 10

print(list(map(add, list1)))
print(list(filter((lambda x: x > 3), list1)))
print(reduce((lambda x, y: x + y), list1))
print(filter((lambda x: x > 3), list1))
