class Adderv3: # dodawanie w miejscu
    def __init__(self, val):
        self.val = val

    def __iadd__(self, other):
        self.val += other
        return self


x = Adderv3(5)
x += 1
x += 1
print(x.val)
