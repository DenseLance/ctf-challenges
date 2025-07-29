# back to roots

<p align = "center"><img src="challenge.JPG" alt="alt text" width="50%" height="50%" /></p>

The challenge says we get the value of a number's square root. Hmm, that should be easy! Wait a minute... why do they only give the values after the decimal place?

```python
from random import randint
from decimal import Decimal

K = randint(10**10, 10**11)
print('K', K)
leak = int(str(Decimal(K).sqrt()).split('.')[-1])
```

This yields `leak = 0.4336282047950153046404`. No matter, a simple exhaustive search gives us the answer fairly quickly.

```python
c = bytes.fromhex("7863c63a4bb2c782eb67f32928a1deceaee0259d096b192976615fba644558b2ef62e48740f7f28da587846a81697745")
for sq in range(int(Decimal(10**10).sqrt()), int(Decimal(10**11).sqrt()) + 1):
    K = (sq + leak) ** 2
    if abs(round(K) - K) < 0.000001:
        print(AES.new(md5(f"{round(K)}".encode()).digest(), AES.MODE_ECB).decrypt(c))
```

We obtain the flag as one of the possible answers:

```
uiuctf{SQu4Re_Ro0T5_AR3nT_R4nD0M}
```