import z

z.x = 30

z.y[0] = 50

print(z.x)

print(z.y)


l = list(z.__dict__)

print(l)

m = list(name for name in z.__dict__ if not name.startswith('__'))

print(m)
