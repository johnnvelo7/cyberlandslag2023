from hashlib import *

c = "0123456789-"
flippy = lambda x: bytes.fromhex((m := x.encode().hex())[1::2] + m[::2])
check1 = lambda x: exit(-1) if len(x) < 16 else None
check2 = (
    lambda x: exit(-2)
    if not (
        all(e in c for e in x)
        and len(x) == 29
        and x[5::6] == "-" * 4
        and x.count("-") == 4
    )
    else None
)
check3 = (
    lambda x, y: exit(-3)
    if not all(
        f(flippy(x)).hexdigest().startswith(g)
        for f, g in zip([md5, sha1, sha256, sha384, sha512], y.split("-"))
    )
    else None
)

name, secret = map(input, ["What's your name?\n> ", "What's your secret?\n> "])
check1(name)
check2(secret)
check3(name, secret)
print(open("flag.txt").read())
