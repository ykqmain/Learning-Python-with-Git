x = 1
l = [1, 2]


def changer(a, b):
    a = 2
    b[0] = 'abc'


changer(x, l)

print(x, l)


def f1(a, b, c):
    print(a, b, c)


f1(1, 2, 3)

f1(2, c=4, b=6)


def f2(a, b=2, c=3):
    print(a, b, c)


f2(1, 3)


def f3(*x):
    print(x)


f3()
f3(1)
f3(1, 3, 5)
f3(1, 'abc')


def f4(**d):
    print(d)


f4()
f4(a=1, dd=f3(1))
