class DongWu:

    l = 0
    h = 0

    def wai(self, l, h):
        print(l, h)

    def chi(self):
        print('吃')

    def shui(self):
        print('睡')


class Gou(DongWu):
    def display(self, x):
        print(x)


x = Gou()

x.chi()
x.display(1)

x.l = 0.5
x.h = 50
x.wai(x.l, x.h)

