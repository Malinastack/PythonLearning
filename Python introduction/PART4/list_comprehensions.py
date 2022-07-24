f = open('script2.py')
lines = f.readlines()

lines = [x.rstrip() for x in lines]

print(lines)

# krocej

lines2 = [x.rstrip() for x in open('script2.py')]

print(lines2)

lines3 = [x.rstrip() for x in open('script2.py') if x[0] =='p']

print(lines3)

print([x + y for x in 'abc' for y in 'lmn'])

S = 'hello'
Y = 'brown'
L = {ix: x for ix, x in enumerate(S)}
print(L)
print(type(L))

X = {key: value for key, value in zip(S, Y)}
print(X)

print({ix: line for ix, line in enumerate(open('script2.py')) if line[0] == 'p'})