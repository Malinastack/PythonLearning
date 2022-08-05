class Super:
    """
    W tej metodzie wykorzystujemy wywolanie metody z klasy podrzednej (Provider.action) 
    """
    def method(self):
        print('Super.method')

    def delegate(self):
        self.action()


class Inheritor(Super):
    pass


class Replacer(Super):
    def method(self):
        print('Replacer method')


class Extender(Super):
    def method(self):
        print('początek Extender.method')
        Super.method(self)
        print('koniec Extender.method')


class Provider(Super):
    def action(self):
        print('Provider.action')


if __name__ == '__main__':
    for klasa in (Inheritor, Replacer, Extender):
        print('\n' + klasa.__name__ + '...')
        klasa().method()
    print('\n', Provider)
    x = Provider()
    x.delegate()
