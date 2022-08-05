from squares import Squares

for i in Squares(1, 5):
    print(i, end=' ')

# x = Squares(1, 5)
# I = iter(x)
# print(next(I))

x = Squares(1, 8)
print()
print(tuple(x), tuple(x))