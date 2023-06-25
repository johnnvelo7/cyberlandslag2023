from Cryptodome.Util.number import long_to_bytes, isPrime, getPrime
import random
import os

# Step 1: Read the encrypted data from file
with open("output.txt", "rb") as f:
    ct = int.from_bytes(f.read(), byteorder="big")

# Step 2: Generate random prime p
def generate_random_prime():
    while True:
        # Generate 33 32-bit random numbers and add them to a list
        random.seed(os.urandom(1024))
        bits = [random.getrandbits(32) for _ in range(33)]

        # Discard 364 32-bit random numbers
        random.getrandbits(364*32)

        # Generate 32 more 32-bit random numbers and add them to the list
        bits += [random.getrandbits(32) for _ in range(32)]

        # Discard 195 32-bit random numbers
        random.getrandbits(195*32)

        # Generate a 1024-bit random number n and check if it's prime
        n = random.getrandbits(1024)
        if isPrime(n):
            break

    return bits, n

# Step 3: Generate random prime q and compute n
q = getPrime(1024)
bits, p = generate_random_prime()
n = p * q

# Step 4: Compute private key d and decrypt the data
e = 0x10001
phi = (p-1) * (q-1)
d = pow(e, -1, phi)
pt = pow(ct, d, n)

# Step 5: Save the decrypted data to file
with open("decrypted.txt", "rb") as f:
    data = f.read()

encodings = ["utf-8", "latin-1", "iso-8859-1", "cp1252", "ascii"]
for enc in encodings:
    try:
        text = data.decode(enc)
        print(f"{enc}: {text}")
    except UnicodeDecodeError:
        pass


