import math
L = [2, 4, 9, 16, 25]

res = []
for i in L:
    res.append(math.sqrt(i))
print(res)

L2 = list(map(math.sqrt, L))
print(L2)

L3 = [math.sqrt(x) for x in L]
print(L3)

L4 = (math.sqrt(x) for x in L)
print(list(L4))