class Empty:
    def __getattr__(self, attrname):
        if attrname == 'age':
            return 40
        else:
            raise AttributeError

x = Empty()
print(x.age)
# print(x.name)

class Accesscontrol:
    def __setattr__(self, key, value):
        if key == 'age':
            self.__dict__[key] = value + 10
        else:
            raise AttributeError(key + ' nie jest dozwolony')


x = Accesscontrol()
x.age = 40
print(x.age)