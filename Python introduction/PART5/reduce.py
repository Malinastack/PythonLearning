from functools import reduce

print(reduce((lambda x, y: x + y), [1, 2, 3, 4]))

print(reduce((lambda x, y: x * y ), [1, 2, 3, 4]))

# to samo co

L = [1, 2, 3, 4]

res = L[0]
for x in L[1:]:
    res = res + x

print(res)


def myreduce(function, sequence):
    tally = sequence[0]  # bierzemy pierwszy element listy
    for next_item in sequence[1:]: # bierzemy po kolei elementy listy poza pierwszym
        tally = function(tally, next_item) # w zaleznosci od funkcji dodajemy/mnozymy etc.. pierwszy z nastepnym itd.
    return tally


print(myreduce((lambda x, y: x * y ), [1, 2, 3, 4, 5]))