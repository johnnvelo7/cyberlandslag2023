import base64
import hashlib
from Cryptodome.Cipher import AES

def encrypt(plaintext, aesKey, macKey):
    aes = AES.new(base64.b64decode(aesKey), AES.MODE_CBC)
    plainBytes = plaintext.encode('utf-8')
    padBytes = 16 - len(plainBytes) % 16
    plainBytes += bytes([padBytes] * padBytes)
    cipherBytes = aes.encrypt(plainBytes)
    macBytes = hashlib.sha256(aes.iv + cipherBytes + base64.b64decode(macKey)).digest()
    macBytesB64 = base64.b64encode(macBytes).decode('utf-8')
    ivB64 = base64.b64encode(aes.iv).decode('utf-8')
    cipherBytesB64 = base64.b64encode(cipherBytes).decode('utf-8')
    return f"{macBytesB64}:{ivB64}:{cipherBytesB64}"

def decrypt(ciphertext, aesKey, macKey):
    ciphertext = ciphertext.strip()  # Remove newline characters
    macB64, ivB64, cipherBytesB64, aesKeyB64 = ciphertext.split(":")
    macBytes = base64.b64decode(macB64.encode('utf-8'))
    aes = AES.new(base64.b64decode(aesKey), AES.MODE_CBC, base64.b64decode(ivB64))
    cipherBytes = base64.b64decode(cipherBytesB64.encode('utf-8'))
    plainBytes = aes.decrypt(cipherBytes)
    padBytes = plainBytes[-1]
    plainBytes = plainBytes[:-padBytes]
    computedMacBytes = hashlib.sha256(base64.b64decode(ivB64.encode('utf-8')) + cipherBytes + base64.b64decode(macKey)).digest()
    print("Computed MAC:", base64.b64encode(computedMacBytes).decode('utf-8'))
    print("Ciphertext:", ciphertext)
    print("Plaintext:", plainBytes.decode('utf-8'))
    print("AES Key:", aesKey)
    print("MAC Key:", macKey)
    if computedMacBytes != macBytes:
        raise ValueError("MAC check failed")
    return plainBytes.decode('utf-8')




# Example usage
aesKey = "x7HC2RIdC2wr5ur5U4LgDg=="
macKey = "v7KlPN+LhhbTuhdRb/Q90uDHyz7IA+sLj6PZWbpqY9fqZFCOx+OL1xebzgAjmtxw"
ciphertext = "Zk1CiyMcds495Uze1JRSaoQUGRqJmr0pOsSKeqziXCg=:x7HC2RIdC2wr5ur5U4LgDg==:v7KlPN+LhhbTuhdRb/Q90uDHyz7IA+sLj6PZWbpqY9fqZFCOx+OL1xebzgAjmtxw:TzIgZUcwdGJSTTpxKWJUNTN7P1lPMDFcQkBsXW83Ojo="
plaintext = decrypt(ciphertext, aesKey, macKey)
print(plaintext)

