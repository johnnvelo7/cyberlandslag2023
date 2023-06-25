from sage.all import *
from Cryptodome.Util.number import bytes_to_long, long_to_bytes

p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
F = GF(p)
secp256k1 = EllipticCurve(GF(p), [0, 7])
n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141

def decrypt(ct, d):
    pt = d * secp256k1(ct[0], ct[1])
    m = Integer(pt.xy()[0])
    return long_to_bytes(m)


e = 65537
d = inverse_mod(e, n)
ct = (108057966156216802984584775718998704019908362174182772193959370371375834561308, 6923544238723742250204021614306336839476506348258026194109794197973309698113)
pt = decrypt(bytes_to_long(ct), d)

print(f"pt = {pt}")
