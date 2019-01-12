import builtins


def mi(a, b):
    return a**b


print(mi(4, 0.5))


def jiaoji(s1, s2):
    s = []
    for x in s1:
        if x in s2:
            s.append(x)
    return s


s1 = [1, 2, 3, 4]

s2 = (2, 4, 6, 8)

print(jiaoji(s1, s2))

print([x for x in s1 if x in s2])


x = 10


def func(y):
    return x*y    # LEGB规则


print(func(2))


def func2(y):
    x = 1
    return x*y


print(func2(2), x)


print(len(dir(builtins)))

# len([x for x in dir(builtins) if not x.startwith('__')]))


z = 10


def func3(y):
    global z
    z = 5
    return y*z


print(func3(5), z)