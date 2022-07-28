# najpierw przyklad z petla
# najpierw sposob z map/filter
# potem sposob z list comprehension

res = []
for x in 'spam':
    res.append(ord(x))
print(res)
# sposob z funkcja map
res2 = list(map(ord, 'spam'))
print(res2)
# sposob z lista skladana
res3 = [ord(x) for x in 'spam'] # najlepszy sposob
print(res3)



condemnation = list(map((lambda x: x**2), range(10)))
print(condemnation)
condemnation2 = [x ** 2 for x in range(10)]
print(condemnation2)

res = []
for x in range(5):
    if x % 2 == 0:
        res.append(x)
print(res)

res2 = list(filter((lambda x: x % 2 == 0), range(5)))
print(res2)

res3 = [x for x in range(5) if x % 2 == 0]
print(res3)


# jeden z lepszych przykladow dlaczego list comprehension wygrywa

answer = [x ** 2 for x in range(10) if x % 2 == 0]
print(answer)

answer2 = list(map((lambda x: x**2), filter((lambda x: x % 2 ==0), range(10))))
print(answer2)

print(list(map((lambda x, y: x + y), [1, 2, 3, 4], [2, 3, 4, 5])))