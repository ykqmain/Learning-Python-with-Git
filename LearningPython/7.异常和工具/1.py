def fetcher(obj, index):
    return obj[index]


x = 'abc'
print(fetcher(x, 2))


try:
    print(fetcher(x, 4))
except IndexError:
    print('got exception')

print('继续')

try:
    raise IndexError
except IndexError:
    print('got exception')

try:
    print(fetcher(x, 2))
finally:
    print('after fetch')