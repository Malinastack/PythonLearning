from abc import ABCMeta, abstractmethod


class Super(metaclass=ABCMeta):

    def delegate(self):
        self.action()

    @abstractmethod
    def action(self):
        pass


# X = Super() # Can't instantiate abstract class Super with abstract methods delegate

class Sub(Super):
    def action(self):
        print('raspberry')


X = Sub()
X.delegate()