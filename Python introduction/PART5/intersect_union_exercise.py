def intersect(*args):
    res = []
    for x in args[0]:
        if x in res:
            continue
        for other in args[1:]:
            print(x)
            print(other)
            if x not in other or x in res:
                break
            else:
                res.append(x)

    for x in res:
        for other in args:
            if x not in other:
                res.remove(x)
    return res


def union(*args):
    res = []
    for seq in args:
        for x in seq:
            if x not in res:
                res.append(x)

    return res

s1, s2, s3 = 'Teodor', 'Teofil', 'Troll'
print(intersect(s1, s2))
print(union(s1,s2))


def func(a, b, c):
    a = 2
    b[0] = 'x'
    c['a'] = 'y'


l = 1
m=[1]
n={'a': 0}

print(func(l, m, n))
print(l, m ,n)
