R = range(3)
I1 = iter(R)
I2 = iter(R)

print(next(I1))
print(next(I1))
print(next(I2))
print(next(I2))
print(next(I1))


Z = zip((1, 2, 3), (11, 12, 13))
I1 = iter(Z)
I2 = iter(Z)
print(next(I1))
print(next(I1))
print(next(I2))  # jest na tej samej pozycji co I2
# print(next(I2)) # koniec iteracji


