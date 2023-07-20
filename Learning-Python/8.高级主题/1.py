print(ord('a'))

print(hex(97))

print(chr(1024))

print(chr(0xc4))


S = 'Unicode'

open('1.txt', 'w', encoding='utf-8').write(S)

print(open('1.txt', 'rb').read())