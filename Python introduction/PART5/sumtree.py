def sumtree(l):
    tot = 0
    for x in l:
        if not isinstance(x, list):
            tot += x
        else:
            print(sumtree(x))
            tot += sumtree(x)
    return tot


L = [1, [2, [3, 4], 5], 6, [7, 8]]
print(sumtree(L))


def sumtree2(l):  # rozwiazanie bez rekurencji
    tot = 0
    items = list(l)
    while items:
        front = items.pop(0)
        if not isinstance(front, list):
            tot += front
        else:
            items[:0] = front
    return tot


L = [1, [2, [3, 4], 5], 6, [7, 8]]
print(sumtree2(L))
