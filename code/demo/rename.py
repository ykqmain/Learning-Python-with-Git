#!/usr/bin/env python3

import os


print("当前路径："+os.getcwd())

files = os.listdir(os.getcwd())

count = 0
print("将A后缀重命名为B后缀")
A = input("A = ")
B = input("B = ")

for filename in files:
    portion = os.path.splitext(filename)

    # print(portion)
    if portion[1] == ("." + A):
        count += 1
        # 重新组合文件名和后缀名
        newname = portion[0] + "." + B
        try:
            print("将", filename, "重命名为", newname)
            os.rename(filename, newname)
        except FileExistsError:
            print('文件已存在')

print("*"*20, "\n修改了", count, "个文件")

