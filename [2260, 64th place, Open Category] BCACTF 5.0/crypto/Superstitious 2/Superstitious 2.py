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
