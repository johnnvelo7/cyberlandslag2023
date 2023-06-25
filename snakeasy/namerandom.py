import random
import string
from hashlib import *

flippy = lambda x: bytes.fromhex((m := x.encode().hex())[1::2] + m[::2])

# Generate a random name
#name = ''.join(random.choice(string.ascii_letters) for _ in range(10))
name = "abcdefghijklmnop2"

secret = "24316-73066-91363-03532-83616"
# Generate a random secret with valid format
#secret = ''.join(random.choice("0123456789-") for _ in range(29))
#secret = secret[:5] + '-' + secret[5:]

# Encode the name using flippy and compute the hashes
hashes = []
for f in [md5, sha1, sha256, sha384, sha512]:
    hash = f(flippy(name)).hexdigest()
    hashes.append(hash)

# Check if the hashes match the hashes in the secret
if all(hash.startswith(h) for hash, h in zip(hashes, secret.split('-'))):
    print("Valid input:")
    print("Name:", name)
    print("Secret:", secret)


print("Valid input:")
print("Name:", name)
print("hashes:", hashes)
print("Secret:", secret)
