def permute1(seq):
    if not seq:
        return [seq]
    else:
        res = []
        for i in range(len(seq)):
            rest = seq[:i] + seq[i+1:]
            for x in permute1(rest):
                print('seq:', seq[i:i + 1], 'x:', x)
                res.append(seq[i:i+1]+x)
        return res





def permute2(seq):
    if not seq:
        yield seq
    else:
        res = []
        for i in range(len(seq)):
            rest = seq[:i] + seq[i+1:]
            print(i, rest)
            for x in permute2(rest):
                print('seq:', seq[i:i+1] , 'x:',  x)
                yield seq[i:i+1] + x


sth = permute2('spam')
print(next(sth))
print(next(sth))
print(next(sth))
print(next(sth))
