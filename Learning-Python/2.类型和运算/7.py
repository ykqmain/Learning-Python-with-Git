l1 = ['pythoon']

l2 = ['list']

l3 = [3]

print(l1 + l2 + l3 * 4 + list('.'), len(l1 + l2 + l3))

print(3 in l3, 3 is l3)

l4 = [1, 2, 3, 4, 5]

l4[3] = 10

l4.append(11)

l4.extend([6, 7, 8, 9])

l4.insert(3, 100)

l4.remove(9)

del l4[2]

print(l4)

for x in l4[::-1]:
    print(x)

print(l4.pop(2))

l4.reverse()

print(l4.index(6))