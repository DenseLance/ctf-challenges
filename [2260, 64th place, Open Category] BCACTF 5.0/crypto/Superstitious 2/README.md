<p align = "center"><img src="challenge.JPG" alt="alt text" width="75%" height="75%" /></p>

Picky with primes? It can't be that bad, right? I saw the process of how the primes `p` and `q` were generated and was in utter shock.

```
def myGetPrime():
    while True:
        x = getRandomNBitInteger(1024) & ((1 << 1024) - 1)//3
        if isPrime(x):
            return x
```

It should be noted that `(1 << 1024) - 1) // 3` is equal to `0b10101010....101`. Combined with the bitwise `&` operator, we can deduce 2 pieces of information:

1. `p` and `q` each have a maximum of 1023 bits.

2. Every alternate bit of `p` and `q` would always be 0.

My first idea was to use the [Coppersmith Method](https://en.wikipedia.org/wiki/Coppersmith_method), since half of the bits of `p` and `q` are known to be 0. Howeve, I tried using sagemath and gmpy2, but both modules did not give me any valid solutions (probably because I'm too dumb to understand the concept).

I ventured out on Google and stumbled upon this [research paper](https://hal.science/hal-03045663/document), where it describes how RSA can be attacked given a sufficient number of non-contiguous bits of `p` and `q`.

<p align = "center"><img src="research paper 1.JPG" alt="alt text" width="75%" height="75%" /></p>

The paper mentions that a branch and prune algorithm would be able to solve for the unknown bits of both primes, with the branching factor = 2 for unknown bits, and converges back to 1 when known bits are reached. Pruning is also done automatically by removing nodes which do not satisfy the condition `(LSB(p, i) * LSB(q, i)) % pow(2, i) == LSB(n) % pow(2, i)`, where `i` equals to the current depth of the traversed tree.

<p align = "center"><img src="research paper 2.JPG" alt="alt text" width="75%" height="75%" /></p>

As suggested by the paper, we use a depth-first search which provided greater efficiency. Our code, as shown below, is a complete implementation and can be used in other situations where the bit pattern of `p` and `q` are non-standard.

```python
from Crypto.Util.number import *

c = 12785320910832143088122342957660384847883123024416376075086619647021969680401296902000223390419402987207599720081750892719692986089224687862496368722454869160470101334513312534671470957897816352186267364039566768347665078311312979099890672319750445450996125821736515659224070277556345919426352317110605563901547710417861311613471239486750428623317970117574821881877688142593093266784366282508041153548993479036139219677970329934829870592931817113498603787339747542136956697591131562660228145606363369396262955676629503331736406313979079546532031753085902491581634604928829965989997727970438591537519511620204387132
e = 65537
n = 550201148354755741271315125069984668413716061796183554308291706476140978529375848655819753667593579308959498512392008673328929157581219035186964125404507736120739215348759388064536447663960474781494820693212364523703341226714116205457869455356277737202439784607342540447463472816215050993875701429638490180199815506308698408730404219351173549572700738532419937183041379726568197333982735249868511771330859806268212026233242635600099895587053175025078998220267857284923478523586874031245098448804533507730432495577952519158565255345194711612376226297640371430160273971165373431548882970946865209008499974693758670929
probable_bits = ((1 << 1024) - 1) // 3

def branch_and_prune(n: int, str_p: str, str_q: str):
    # Section 4.3.1 of https://hal.science/hal-03045663/document
    max_bit_len = max(len(str_p), len(str_q)) + 1
    str_p, str_q = str_p.zfill(max_bit_len), str_q.zfill(max_bit_len)
    stack = [[str_p[-1], str_q[-1]]]
    while stack:
        partial_p, partial_q = stack.pop() # paper suggests DFS
        if len(partial_p) == max_bit_len: # final check
            if int(partial_p, 2) * int(partial_q, 2) == n:
                return partial_p[1:], partial_q[1:]
        else:
            possible_p, possible_q = [], []
            if partial_p[0] == "_":
                possible_p.append("1" + partial_p[1:])
                possible_p.append("0" + partial_p[1:])
            else:
                possible_p.append(partial_p)
            if partial_q[0] == "_":
                possible_q.append("1" + partial_q[1:])
                possible_q.append("0" + partial_q[1:])
            else:
                possible_q.append(partial_q)
            modulo = 2 ** len(possible_p[0]) # constraint
            for poss_p in possible_p:
                for poss_q in possible_q:
                    if (int(poss_p, 2) * int(poss_q, 2)) % modulo == n % modulo:
                        stack.append([str_p[-len(poss_p)-1] + poss_p,
                                      str_q[-len(poss_q)-1] + poss_q])
    if len(stack) == 0:
        raise Exception("No Solution Found.")

str_p = bin(probable_bits)[2:].replace("1", "_")
str_q = str_p

str_p, str_q = branch_and_prune(n, str_p, str_q)
p, q = int(str_p, 2), int(str_q, 2)

assert p * q == n
print("p:", p)
print("q:", q)

phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)
m = pow(c, d, n)
print("Flag:", long_to_bytes(m).decode())
```

Using a tree search, we were able to obtain `p` and `q`:

```
p: 47981816076831973450909530669541706953770597006817333749891020556945477629662108524163405141438024312107792294535273473111389298189846712963818162954497000930546383005418285868804270188594230163069868709422261521819309406460567627868198499351382463630966329988388255592530605189569811432880392671877694493697
q: 11466867937506443031079406557463511000236825156042986330491372554263065048494616429572254582549332374593524344514321333368747919034845244563606383834070804967345648840205613712911286600828703809116499141392947298788689558078395325755136448592591616295144118450804581480471547613492025968699740517273286296657
```

We then output the flag:

```
bcactf{l4zy_cHall3nG3_WRITinG_f8b335319e464}
```