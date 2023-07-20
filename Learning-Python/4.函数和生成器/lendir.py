def lendir_num(t):
    a = len(dir(t))
    b = len([x for x in dir(t) if not x.startswith('__')])
    return a, b


print(lendir_num(list))