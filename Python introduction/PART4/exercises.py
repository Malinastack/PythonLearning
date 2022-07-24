# zadanie1
S = 'hello'
S2 = [ord(c) for c in S]
sum = sum(S2)
print(sum)
print(list(map(ord, S)))
# zadanie2
for i in range(50):
    print('Witaj %d\n\a' % i)

D = dict(b=5, c=2, a=1, d=3, e=4)
# zadanie3
for k, v  in sorted(D.items()):
    print(f'Key: {k}\n'
          f'Value: {v}')

# zadanie4
L = [1, 2, 4, 8, 16, 32, 64]
X = 5


# i = 0
# while i < len(L):
#     if 2 ** X == L[i]:
#         print('Pod indeksem:', i)
#         break
#     else:
#         i = i + 1
#
# else:
#     print(X, 'nie odnaleziono')


# for i in range(len(L)):
#     if 2 ** X == L[i]:
#         print('Pod indeksem:', i)
#         break
# else:
#     print(X, 'nie odnaleziono')

if 2**X in L:
    print('Pod indeksem:', L.index(2**X))
else:
    print('Nie odnaleziono')

L = []

for i in range(10):
    L.append(2**i)

print(L)

L2 = list(map(lambda x: 2**x, range(10)))
print(L2)