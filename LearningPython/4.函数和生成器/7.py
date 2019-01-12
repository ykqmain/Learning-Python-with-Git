print(ord('s'))

res = []
for x in 'abc':    # for循环
    res.append(ord(x))

print(res)


res = list(map(ord, 'abc'))    # map函数
print(res)

res = [ord(x) for x in 'abc']    # 列表推导
print(res)


print(list(filter((lambda x:x%2==0), range(5))))

l = [x**2 for x in range(10) if x % 2 ==0]
print(l)
