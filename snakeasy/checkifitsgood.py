from hashlib import *

x = "XAXczgM0FDYRJXJkcwBaUIwfEW"
y = "23552-10195-83583-84291-83583"

#x = "abcdefghijklmnopH"
#y = "1455f-0562f-06261-65762-05228"

#x = "abcdefghijklmnop2"
#y = "29890-76741-90970-00f34-81436"


flippy = lambda x: bytes.fromhex((m:=x.encode().hex())[1::2]+m[::2])
hash_functions = {"MD5": md5, "SHA-1": sha1, "SHA-256": sha256, "SHA-384": sha384, "SHA-512": sha512}

for name, f, g in zip(hash_functions.keys(), hash_functions.values(), y.split("-")):
    hash_value = f(flippy(x)).hexdigest()
    if hash_value.startswith(g):
        print(f"{name}:   {hash_value} ITS GOOD NOW")
    else:
        print(f"{name}:   {hash_value} NOT GOOD")
