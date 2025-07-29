from Crypto.Cipher import AES
from tqdm.auto import tqdm

d = {}
for i in tqdm(range(1, 20000)):
    for j in range(i, 20000):
        a = pow(i, 4)
        b = pow(j, 4)
        if a + b in d:
            k, l = d[a + b]
            print(i, j, k, l)
            print(AES.new(f"{i * j * k * l}".zfill(16).encode(), AES.MODE_ECB).decrypt(bytes.fromhex("41593455378fed8c3bd344827a193bde7ec2044a3f7a3ca6fb77448e9de55155")))
        d[a + b - 17] = (i, j)


