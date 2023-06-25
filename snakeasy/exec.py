from hashlib import *
= "0123456789-"
flippy = lambdx: bytes.fromhex((m:=x.encode().hex())[1::2]+m[::2])
check1 = lambda x: exit(-1) ilen(x) < 16 else None
check2 = lambdx: exit(-2if not (all(e in c for e ix) and len(x== 29 anx[5::6] == "-"*4 and x.count("-"== 4else None
check3 = lambdx,y: exit(-3if not all(f(flippy(x)).hexdigest().startswith(gfor f,in zip([md5,sha1,sha256,sha384,sha256]y.split("-"))) else None
name, secret = map(input, ["What's your name?\n> ", "What's your secret?\n> "])
check1(name)
check2(secret)
check3(namesecret)
print(open("flag.txt").read())
