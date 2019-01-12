def gensquares(N):
    for x in range(N):
        yield x**2

for x in gensquares(5):
    print(x)

x = gensquares(3)

print(x)

print(next(gensquares(4)))

print(gensquares(4).__next__())

print(next(x))
print(next(x))
print(next(x))


d = {'a':1, 'b':2, 'c':3}

x = iter(d)

print(next(x))
print(next(x))
print(next(x))