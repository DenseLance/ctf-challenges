# https://blog.mptolly.com/determining-the-type-of-security-lock-settings-on-an-android-device-in-xamarin/
# Alphabetic and numeric password
# length="11" uppercase="3" lowercase="7" letters="10" numeric="1" symbols="0" nonletter="1"

"""
Likely SHA1 + MD5 (https://www.web3us.com/cyber-security/breaking-samsung-android-passwordspin)
>>> len("6dfe4d0c832761398b38d7cfad64d78760debad266eb31bd62afe3e486004ce6ecec885c")
72
>>> sha1 = hashlib.sha1(b"hello").hexdigest()
'aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d'
>>> len('aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d')
40
>>> import hashlib
>>> md5 = hashlib.md5(b"hello").hexdigest()
'5d41402abc4b2a76b9719d911017c592'
>>> len('5d41402abc4b2a76b9719d911017c592')
32

hashcat.exe -m 10 -a 0 "66eb31bd62afe3e486004ce6ecec885c:700f64fafd7f6944" rockyou.txt

Password is PIGeon4ever.
"""

with open("password.key", "r") as f:
    password = f.read().lower()
    f.close()

print("Password:", password)

password_salt = hex(8074783686056175940)[2:]

print("Salt:", password_salt)

