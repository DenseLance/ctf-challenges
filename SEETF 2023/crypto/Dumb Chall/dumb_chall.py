from pwn import *

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

target = remote("win.the.seetf.sg", 3002)
multiplier = 1
for i in range(30):
    received = b""
    while b":" not in received:
        received += target.recv(4096)
    received = received.decode().split("\n")
    is_r = "w" not in received[-1]
    r = int(is_r) * i
    r += 1
    print(received)

    for line in received:
        try:
            exec(line)
        except:
            break

    assert y < p # y = pow(g, x, p)
    assert g < p # Gambling with Qingque be liek
    target.sendline(str(r))

    received = b""
    while b":" not in received:
        received += target.recv(4096)
    print(received)

    if is_r:
        target.sendline(str(pow(g, r, p)))
    else:
        # y * c % p = (y * c) % p = g
        target.sendline(str(modinv(y, p) * g * multiplier))
        multiplier *= (p + 1)

received = b""
while b"flag" not in received:
    received += target.recv(4096)
print(received.decode())

target.close()

"""
You passed round 30.
You were more likely to get hit by lightning than proof correctly 30 times in a row, you must know the secret right?
A flag for your troubles - SEE{1_571ll_h4v3_n0_kn0wl3d63}
"""
