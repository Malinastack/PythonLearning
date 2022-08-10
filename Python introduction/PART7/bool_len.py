class Truth:
    def __bool__(self):
        return True


x = Truth()
if x:
    print('tak!')


class Len:
    def __len__(self):
        return 0


x = Len()
if not x:
    print('nie')