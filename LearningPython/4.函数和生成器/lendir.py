def lendir_num(t):
    return len(dir(t)), len([x for x in dir(t) if not x.startwith('__')])
