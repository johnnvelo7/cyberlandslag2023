import hashlib
from hashlib import sha256

name = "abcdefghijklmnop2"
flipped_name = bytes.fromhex((m := name.encode().hex())[1::2] + m[::2])
hash_value = sha256(flipped_name).hexdigest()

print("FIRST HASH IS", hash_value)

my_string = "hello"

# Generate the MD5 hash
md5_hash = hashlib.md5(my_string.encode()).hexdigest()

# Generate the SHA1 hash
sha1_hash = hashlib.sha1(my_string.encode()).hexdigest()

# Generate the SHA256 hash
sha256_hash = hashlib.sha256(my_string.encode()).hexdigest()

# Generate the SHA384 hash
sha384_hash = hashlib.sha384(my_string.encode()).hexdigest()

# Generate the SHA512 hash
sha512_hash = hashlib.sha512(my_string.encode()).hexdigest()

# Print the hash values
print("MD5 Hash:", md5_hash)
print("SHA1 Hash:", sha1_hash)
print("SHA256 Hash:", sha256_hash)
print("SHA384 Hash:", sha384_hash)
print("SHA512 Hash:", sha512_hash)

