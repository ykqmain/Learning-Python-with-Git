def mysum(l):
    # print(l)
    if not l:
        return 0
    else:
        return l[0]+mysum(l[1:])    # 递归


l = [1, 2, 3, 4]

print(mysum(l))
