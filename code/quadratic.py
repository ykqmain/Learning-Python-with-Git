#!/usr/bin/env python3
# chmod +x quadratic.py

# 二次方程, ax^2+bx+c=0, 其中,a不为0描述的是抛物线.这一方程的根可以由公式
# x=(-b±√b^2-4ac)/2a 得出,其中,公式的b^2-4ac 部分被称为判别式

import math

print("ax^2+bx+c=0")

a = float(input("a= "))
b = float(input("b= "))
c = float(input("c= "))

str = "{}x^2+{}x+{}=0"
print(str.format(a, b, c))

d = ((b * b) - (4 * a * c))
print('d = ', d)

if d >= 0:
    root = math.sqrt(d)
    x1 = (-b + root) / (2 * a)
    x2 = (-b - root) / (2 * a)

    if d == 0:
        print("x1 = x2 =", x1)
    else:
        print("x1 =", x1, "x2 =", x2)
else:
    print("无解")
