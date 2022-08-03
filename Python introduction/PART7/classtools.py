class AttrDisplay:
    """
    Udostępnia dziedziczoną metodę przeciążania wyświetlania, która pokazuje instancje z ich nazwami klas, a także parę,
    nazwa=wartość dla każdego atrybutu przechowanego w samej instancji (ale nie atrybutów odziedziczonychpo klasach)
    Można ją wmieszać w dowolną klasę i będzie działała na dowolnej instancji
    """
    def gatherattrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append(f'{key} = {getattr(self, key)}')
        return ', '.join(attrs)

    def __repr__(self):
        return f'{self.__class__.__name__}: {self.gatherattrs()}'


class Toptest(AttrDisplay):
    count = 0

    def __init__(self):
        self.attr1 = Toptest.count
        self.attr2 = Toptest.count +1
        Toptest.count += 2





class Subtest(Toptest):
    pass


class Sub2test(Toptest):
    pass


if __name__ == '__main__':

    X, Y, Z = Toptest(), Subtest(), Sub2test()
    print(X)
    print(Y)
    print(Z)