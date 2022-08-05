class Super:
    """
    W tej metodzie wykorzystujemy wywolanie metody z klasy podrzednej (Provider.action)
    Sprawdź plik abstract_classes.py ;)
    """
    def method(self):
        print('Super.method')

    def delegate(self):
        self.action()

    def action(self):
        # assert False, 'działanie musi zostac zdefiniowane '
        raise NotImplementedError('działanie musi zostac zdefiniowane')


class Subv1(Super):
    pass

class Subv2(Super):
    def action(self):
        print('I tutaj dziala')


if __name__ == '__main__':

    # x = Super()
    # x.delegate() # blad NotImplementedError
    # x = Subv1()
    # x.delegate() # nadal blad
    x = Subv2()
    x.delegate()

