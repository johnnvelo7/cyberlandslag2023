import base64
from Cryptodome.Cipher import AES
import hashlib
import hmac


def decrypt(encrypted_string, aes_key, mac_key):
    ciphertext_b64, iv_b64, hmac_b64 = encrypted_string.split(':')
    ciphertext = base64.b64decode(ciphertext_b64)
    iv = base64.b64decode(iv_b64)
    hmac_received = base64.b64decode(hmac_b64)

    # Calculate HMAC on ciphertext and IV
    hmac_calculated = hmac.new(mac_key, ciphertext + iv, hashlib.sha256).digest()
    if hmac.compare_digest(hmac_received, hmac_calculated):
        # HMAC verification successful, proceed with decryption
        aes = AES.new(aes_key, AES.MODE_CBC, iv)
        plaintext = aes.decrypt(ciphertext).rstrip(b'\0')
        return plaintext
    else:
        raise ValueError('HMAC verification failed')


def main():
    # Set up the AES and HMAC keys
    aes_key_b64 = '2ZPwoRjAbSe6BCwunZl1WA=='
    mac_key_b64 = 'cX+/guE/DZb6uqyQgi+yca9kCqQLoD/gZ4DnJawVFZc='
    aes_key = base64.b64decode(aes_key_b64)
    mac_key = base64.b64decode(mac_key_b64)

    # Open the encrypted file and decrypt its contents
    with open('encrypted.txt', 'r') as f:
        for line in f:
            encrypted_string = line.strip()
            plaintext = decrypt(encrypted_string, aes_key, mac_key)
            print(plaintext.decode())

