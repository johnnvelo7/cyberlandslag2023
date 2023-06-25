from random import choices
from string import ascii_letters, digits
from hashlib import *

flippy = lambda x: bytes.fromhex((m:=x.encode().hex())[1::2]+m[::2])
hash_functions = {"MD5": md5, "SHA-1": sha1, "SHA-256": sha256, "SHA-384": sha384}
hash_count = len(hash_functions)

while True:
    random_string = ''.join(choices(ascii_letters + digits, k=26))
    hash_values = {}
    for name, f in hash_functions.items():
        hash_value = f(flippy(random_string)).hexdigest()
        if hash_value[:5].isdigit():
            hash_values[name] = hash_value
    if len(hash_values) == hash_count:
        print(f"Found: {random_string} ({hash_values})")
        break

#69714-78154-72971-32345-72971
#1IbBidnwDGObaO91yUpIAYAngj

XAXczgM0FDYRJXJkcwBaUIwfEW

23552-10195-83583-84291-83583
