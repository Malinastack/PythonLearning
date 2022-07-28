def copyDict(d):
    new_dict = {}
    for k, v in d.items():
        new_dict[k] = v

    return new_dict

def copyDictv2(d):
    new_dict = {}
    for k in d:
        new_dict[k] = d[k]

    return new_dict

D1 = dict(a=2, b=3, c=4, d=[1, 2, 3])

D3 = copyDictv2(D1)
D2 = copyDict(D1)
D1['a'] = 10
print(D1)
print(D2)
print(D3)


def adddict(dict1, dict2):
    for k, v in dict2.items():
        dict1[k] = v

    return dict1


def adddictv2(dict1, dict2):
    new_dict = {}
    for k, v in dict1.items():
        new_dict[k] = v
    for k, v in dict2.items():
        new_dict[k] = v

    return new_dict  # tutaj bez zmiany w miejscu

D1 = dict(a=2, b=3, c=4, d=[1, 2, 3])
D4 = dict(f=3, g=4, u=1, c=1, d=[1, 2])
print(adddict(D1, D4))
print(adddictv2(D1, D4))

F = adddictv2(D1, D4)
print(F)
D1['c'] = 500
print(F)


E = adddict(D1, D4)
print(E)
D1['c'] = 222
print(E)

