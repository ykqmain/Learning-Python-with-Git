import dir1.dir1_1

# import dir1.dir2

import dir1.dir2.dir2_1

print(dir1.dir2.dir2_1.x)


from dir1.dir2.dir2_2 import y

y = 10

print(y)


from dir1.dir3.dir3_1 import z as mou

print(mou)