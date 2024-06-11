from pwn import xor
with open('output.txt', 'rb') as f:
    flag = f.read()
    f.close()
one, two = list(str(len(flag)))
a = flag[0:len(flag) // 3]
b = flag[len(flag) // 3:2 * len(flag) // 3]
c = flag[2 * len(flag) // 3:]
c = xor(c, int(one) * int(two))
c = xor(b, c)
b = xor(a, b)
a = xor(c, a)
c = xor(b, c)
b = xor(a, b)
a = xor(a, int(one) + int(two))
print((a + b + c).decode())
