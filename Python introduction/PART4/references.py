a = [1, 2, 3, 4]
b = a
b[1] = 0
print(a)

a = [1, 2, 3, 4]
b = a.copy()
b[1] = 0
print(a)
print(b)