def mysum(L):
    if not L:
        return 0
    else:
        return L[0] + mysum(L[1:])


print(mysum([1,2,3,4,5]))


def silnia(n):
    if n == 0:
        return 1
    else:
        return n * silnia(n-1)


print(silnia(5))





