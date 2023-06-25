from Crypto.Util.number import bytes_to_long

p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
F = GF(p)
secp256k1 = EllipticCurve(GF(p), [0, 7])

def encrypt(message, e):
    m = bytes_to_long(message)
    G = secp256k1.lift_x(F(m))
    return e*G

e = 65537
flag = b"flag{?????}"
ct = encrypt(flag, e)

print(f"ct = {ct.xy()}")
