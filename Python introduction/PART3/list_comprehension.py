M = [[1,2,3],[4,5,6],[7,8,9]]

test = [1,2,3,4,5,6,7,8,9]

col2 = [i[1] for i in M]
print(col2)

even = [i[1] for i in M if i[1]%2==0]
print(even)

# przekątna
diag = [M[i][i] for i in [0,1,2]]
print(diag)

G = (sum(row) for row in M)
print(next(G))
print(next(G))
print(next(G))

s = 'inicjalizacja'

s_dict = {x: ord(x) for x in s}
print(s_dict)

test_dict = dict(imie = 'Katarzyna', nazwisko='Kulmaczewska', wiek=22, płeć='female')
print(test_dict)

f = open('data.txt', 'w')
f.write('Siemka\n')
f.write('To ja\n')

f = open('data.txt', 'r')
text = f.read()
print(text)

print(text.split())


class Worker:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]


pracownik1 = Worker('Adam Psikuta', 2000)
print(pracownik1.lastName())

print(type((2+4, 6/2)))

print(0.1+0.1+0.1 - 0.3)

x=set('abcde')
y=set('bdxyz')

print(x - y)
print(x | y)
print(x & y)

S = set()
print(type(S))

S1 = {1,2,3,4}
S2 = S1 - {1,2,3,4}
print(S2)
print(type(S2))
# S3 = {[1,2,3,4], 5,6} do setu nie można wrzucać obiektów mutowalnych (list, słowników etc.)
# print(S3)
T1 = (1, 2, [1, 2, 3])  # a do tupli można
print(T1)
print(type(T1))
print(type({}))

lista = [1, 2, 3, 4, 1, 1, 1, 2, 3, 4]
list2 = list(set(lista))

a = 20
print('Szesnastkowy')
b = oct(a)
print(b)
print('Ósemkowy')
c = hex(a)
print(c)
print('Dwójkowy')
d = bin(a)
print(d)

e = int(d, 2)
print(e)

L1 = [2, 3, 4]
L2 = L1
L1 = [1, 2, 3]
print(L1)
print(L2)

D1 = {'imie': 'Tomasz', 'nazwisko': 'Test'}
D2 = D1.copy()
D1['imie'] = 'Andrzej'
print(D1)
print(D2)

cos = 'AndrzejGolot'

print(cos)
