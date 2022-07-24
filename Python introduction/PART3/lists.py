list1 = ['h', 'e', 'l', 'l', 'o']
word1 = ''.join(list1)

word2 = 'guys'
print(word1+word2)
print(abs(-1))

L = [1,2,3]
L[1:1] = [6,7] # [1:1] pusty wycinek
print(L) # [1, 6, 7, 2, 3] nie usunieto zadnego elementu
L1 = [1,2,3]
L1[1] = [6,7] # [1, [6, 7], 3] zastepujemy element o indeksie 1 (2)
print(L1)
L2 = [1,2,3]
L2.insert(1, [6,7])
print(L2)
# jesli chcemy wstawic np liste w liste, ale aby byla to jedna lista, nalezy uzyc pustego wycinka np. [1:1] ponieważ
# metoda insert oraz bezposrednie wstawienie poprzez wyrazenie wstawiaja cala liste, a nie jej elementy


L = ['abc', 'ABD', 'aBe']
L.sort(key=str.lower)
print(L)

L1 = ['abc', 'ABD', 'aBe']
x = sorted(L1, key=str.lower)
print(x)

L2 = ['abc', 'ABD', 'aBe']
L2.sort(key=str.lower, reverse=True)
print(L2)

L3 = ['abc', 'ABD', 'aBe']
x = sorted([x.lower() for x in L3], reverse=True)
print(x)

L4 = [1,2,3]
L4.extend([4,5])
print(L4)
L4.append(6)
print(L4)