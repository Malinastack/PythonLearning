class C:
    data = 10

    def __gt__(self, other):
        return self.data > other

    def __lt__(self, other):
        return self.data < other

x = C()
print(x > 15)
print(x < 15)