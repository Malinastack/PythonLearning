counters = [1, 2, 3, 4]

#  map wykonuje wskazaną operacje na każdym elemencie sekwencji i zwraca obiekt iterowalny
def inc(x):
    return x + 10


print(list(map(inc, counters)))

# to samo co

res = []

for x in counters:
    res.append(inc(x))

print(res)

print(list(map((lambda x: inc(x)), counters)))


def mymap(func, seq):
    res = []
    for x in seq:
        res.append(func(x))
    return res


print()
print(list(map(inc, [1, 2, 3])))  # zwraca obiekt iterowalny
print()
print(mymap(inc, [5, 6, 7]))  # zwraca liste
print()
print(list(map(pow, [1, 2, 3], [2, 3, 4])))
print()
print([inc(y) for y in [1, 2, 3, 4]])
print()