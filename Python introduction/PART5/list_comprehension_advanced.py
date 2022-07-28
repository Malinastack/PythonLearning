list1 = [x + y for x in [1, 2, 3] for y in [100, 200, 300]]
print(list1)

list2 = [(x, y) for x in range(5) if x % 2 == 0 for y in range(5) if y % 2 == 1]
print(list2)

M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

print([column[1] for column in M]) # kolumna 2 bierzemy zawsze [1] element w kazdym wierszu

print([M[i][i] for i in range(len(M))]) # przekatna

L = [[1, 2, 3], [4, 5, 6]]
for i in range(len(L)):
    for y in range(len(L[i])):
        L[i][y] += 10

print(L) # zmiana w miejscu

# za pomoca list comprehension

L2 = [[col + 10 for col in row] for row in M]
print(L2)

L3 = [col + 10 for row in M for col in row]

M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]