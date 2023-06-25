from Cryptodome.Util.number import bytes_to_long, inverse, long_to_bytes
from primefac import primefac
from functools import reduce

# Load the bits from the output.txt file
with open("output.txt") as f:
    output = f.read()

bits = [int(x) for x in output.split("bits=")[1].split("\n")[0][1:-1].split(", ")]

# Calculate n
q = list(primefac(bits[-1]))[0]
p = reduce(lambda x, y: (x << 32) | y, bits[:-1])
n = p * q

# Load the ciphertext from the output.txt file
ct = int(output.split("ct=")[1].split("\n")[0])

# Calculate the private key d
phi = (p - 1) * (q - 1)
e = 0x10001
d = inverse(e, phi)

# Decrypt the ciphertext
pt = pow(ct, d, n)
flag = long_to_bytes(pt)

print(flag.decode("latin1"))


