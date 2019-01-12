x = 'while'
while x:
    print(x)
    x = x[1:]
    if x == 'le':
        break
else:
    print('Bye')

for x in ['a', 'abc', 123, {'d': 'v'}]:
    print(x)


items = ['aaa', 111, (4, 5), 2.34]
tests = [111, 3.14]

for key in tests:
    for item in items:
        if item == key:
            print(key, 'was found.')
            break
    else:
        print(key, 'not found.')


for x in range(2, 5):
    print(x)

S = 'python3'
print(len(S))
for x in range(len(S)):
    print(S[x], end=' ')

print('\n')

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = [7, 8, 9]

for (x, y, z) in zip(l1, l2, l3):
    print(x, y, z, '%d+%d+%d=' % (x, y, z), x+y+z)

S = 'wo de python'

for (i, x) in enumerate(S):
    print(x, '计数器：', i)