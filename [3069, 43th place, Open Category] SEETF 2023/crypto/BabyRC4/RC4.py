knownPlaintext = b'a' * 36
knownCiphertext = bytes.fromhex('a5c237b6102db668ce467579c702d5af4bec7e7d4c0831e3707438a6a3c818d019d555fc')
unknownCiphertext = bytes.fromhex('b99665ef4329b168cc1d672dd51081b719e640286e1b0fb124403cb59ddb3cc74bda4fd85dfc')

decrypted = bytearray()
for i in range(0, len(unknownCiphertext)):
    p = knownPlaintext[i % len(knownPlaintext)]
    c1 = knownCiphertext[i % len(knownCiphertext)]
    c0 = unknownCiphertext[i] 
    decrypted.append(p ^ c1 ^ c0)

print(decrypted[::-1])




