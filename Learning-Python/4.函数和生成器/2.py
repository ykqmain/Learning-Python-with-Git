x = 9


def f1():
    x = 8

    def f2():
        print(x)

    f2()


f1()


def f3():
    x = 7

    def f4():
        print(x)

    return f4


action = f3()
action()    # 闭包，或工厂函数