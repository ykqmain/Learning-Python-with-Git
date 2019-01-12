print(open('1.txt').read(), '\n')

for line in open('1.txt'):
    print(line.upper())

afile = open('1.txt')
print(afile.__next__())
print(next(afile))

l = [1, 2, 3]

I = iter(l)

print(I.__next__())
print(next(I)+10)


i = iter(l)
for x in range(len(l)):
    print(next(i))

for x in range(len(l)):
    l[x] = 0
print(l)

l = [x+10 for x in l]
print(l)

l = ['a' for x in l]
print(l)

lines = [line.rstrip() for line in open('1.txt') if line[0] == 1]
print(lines)

str = [x for x in open('1.txt')]
print(str)

