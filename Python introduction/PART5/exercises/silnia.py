import math
import time
from functools import reduce

def silnia(n):
    if n == 0:
        return 1
    else:
        return n * silnia(n-1)

print('\n####MATHFACTORIAl####\n')

t0 = time.time()
print(math.factorial(100))
t1 = time.time()
total = t1 - t0
print(total)
total = 0

print('\n#####RECURSION#####\n')
t0 = time.time()
print(silnia(100))
t1 = time.time()
total = t1 - t0
print(total)
total = 0

print('\n#####REDUCE#####\n')
n = 100
t0 = time.time()
l = reduce((lambda x, y: x*y), range(1, n+1))
t1 = time.time()
total = t1 - t0
print(total)
total = 0
print(l)

print('\n####JUSTWHILE####\n')

x = 100
t0 = time.time()
result = 1
while x:
    result*=x
    x-=1
t1 = time.time()
total = t1 - t0
print(total)
total = 0
print(result)

