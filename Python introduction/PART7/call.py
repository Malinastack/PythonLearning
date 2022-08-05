from tkinter import *
from tkinter import ttk


class Callee:
    def __call__(self, *args, **kwargs):
        print('Wywołanie:', args, kwargs)


C = Callee()
print(C(1, 2, 3))


class Callback:
    def __init__(self, color):
        self.color = color

    def __call__(self):
        print('włącz', self.color)


class Callback2:
    def __init__(self, color):
        self.color = color

    def changeColor(self):
        print('włącz', self.color)


root = Tk()
frm = ttk.Frame(root, padding=10)

cb1 = Callback('niebieski')
cb2 = Callback('zielony')
cb3 = Callback2('niebieski')
cb4 = Callback2('zielony')
frm.grid()
B1 = Button(command=cb1)
B1.grid(column=0, row=0)
B2 = Button(command=cb2)
B2.grid(column=0, row=1)
B3 = Button(command=cb3.changeColor)
B3.grid(column=0, row=2)
B4 = Button(command=cb4.changeColor)
B4.grid(column=0, row=3)
root.mainloop()