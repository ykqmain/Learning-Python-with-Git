count = [1, 2, 3, 4]

updated = []

for x in count:
    updated.append(x +10)

print(updated)


def inc(x):return x+10

print(list(map(inc,count)))

print(list(map((lambda x:x+3), count)))


print(list(range(-5, 5)))

print(list(filter((lambda x:x>0), range(-5, 5))))