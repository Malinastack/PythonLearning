file = open('nowy/tekst.txt')
lines = file.readlines()
for i in lines:
    print(i)
X, Y, Z = 43, 44, 45
S = 'Test'
D = {'a': 1, 'b':2}
L = [1,2,3]
f = open('datafile.txt', 'w')
f.write(S + '\n')
f.write('%s,%s,%s\n' % (X, Y, Z))
f.write(str(L) + '$' + str(D) + '\n')
f.close()

F = open('datafile.txt')
line = F.readline()
print(line)
line = F.readline()
parts = line.split(',')
print(parts)
numbers = [int(P) for P in parts]
print(numbers)
line = F.readline()
print(line)
print(type(line))
parts = line.split('$')
objects = [eval(P) for P in parts] # zamieniamy łancuch znaków w listę i słownik
print(objects)
