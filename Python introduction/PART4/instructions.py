seq = [1, 2, 3, 4]
a, b, c, d, *e = seq
print(e)  # zawsze jesli uzyjemy rozpakowania, a zaden element nie zostanie przypisany to zwroci nam []


while seq:
    front, *seq = seq
    print(front, seq)


seq2 = [3, 4, 5, 6]
a, *b = seq2
print(a, b)
a, b = seq2[0], seq2[1:]
print(a, b)

*a, b = seq2
print(a, b)
a, b = seq2[:-1], seq2[-1]
print(a, b)


seq3 = ['Adam', 'Tomek', 'Adrian']


def hello(*args):
    for i in args:
        for y in i:
            print(y)

hello(seq3)

print(3 and [])
print([] and {})




