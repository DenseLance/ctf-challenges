# https://blog.mptolly.com/determining-the-type-of-security-lock-settings-on-an-android-device-in-xamarin/
# Pattern password
# length="5"

"""
From https://nelenkov.blogspot.com/2015/06/password-storage-in-android-m.html, we get a glipse of the code needed.

Signature: 8c6f2d4d5eb89748ca46b11da509abb1d7a1c80e802ed071c63d5d7ca9109319
Hash: 8c6f2d4d5eb89748ca46b11da509abb1d7a1c80e802ed071c63d5d7ca9109319
Password: 95184

The gesture is 95184.
"""

import struct
import scrypt
from Crypto.Util.number import *

N = 16384
r = 8
p = 1

with open("passwords.txt", "w") as f:
    for a in "123456789":
        for b in "123456789":
            for c in "123456789":
                for d in "123456789":
                    for e in "123456789":
                        password = a+b+c+d+e
                        if len({a,b,c,d,e}) == len(password):
                            f.write(password + "\n")
    f.close()

f = open('gatekeeper.pattern.key', 'rb')
blob = f.read()
f.close()
s = struct.Struct('<'+'17s 8s 32s')
meta, salt, signature = s.unpack_from(blob)
with open("passwords.txt", "r") as f:
    for password in f:
        to_hash = meta
        to_hash += password[:-1].encode()
        h = scrypt.hash(to_hash, salt, N, r, p)

        if h[0:32] == signature:
            print("Signature:", hex(bytes_to_long(signature))[2:])
            print("Hash:", hex(bytes_to_long(h[0:32]))[2:])
            print("Password:", password)
            break
    f.close()
