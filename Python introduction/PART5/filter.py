lista1 = list(range(-5, 5))

print(list(filter((lambda x: x > 0), lista1)))

# to samo co

res = []
for x in range(-5, 5):
    if x > 0:
        res.append(x)

print(res)

# i to samo co

lista2 = [x for x in range(-5, 5) if x > 0]
print(lista2)

