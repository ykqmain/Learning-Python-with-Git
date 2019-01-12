afile = open('f.py', 'w')

str = "\'''hello, python\n" + 'file\n' + "f.py\'''"

afile.write(str)

bfile = open('1.txt', 'r')

print(bfile.read())
