from random import randint
from decimal import Decimal
from hashlib import md5

from Crypto.Cipher import AES

leak = 0.4336282047950153046404
c = bytes.fromhex("7863c63a4bb2c782eb67f32928a1deceaee0259d096b192976615fba644558b2ef62e48740f7f28da587846a81697745")
for sq in range(int(Decimal(10**10).sqrt()), int(Decimal(10**11).sqrt()) + 1):
    K = (sq + leak) ** 2
    if abs(round(K) - K) < 0.000001:
        print(round(K))
        print(AES.new(md5(f"{round(K)}".encode()).digest(), AES.MODE_ECB).decrypt(c))
