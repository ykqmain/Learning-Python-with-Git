s = 'wo de python zhilv'

a, b, *c = s.split(' ')

print(a, b, end='\n')

afile = open('1.txt', 'w')

print(b, c, end='\n', file=afile)
