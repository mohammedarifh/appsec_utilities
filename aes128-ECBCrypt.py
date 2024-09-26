import sys
from Crypto.Cipher import AES
import base64

def pad(s):
    # Padding to ensure the data is a multiple of 16 bytes (AES block size)
    return s + (16 - len(s) % 16) * chr(16 - len(s) % 16)

def unpad(s):
    # Remove the padding at the end of the data
    return s[:-ord(s[len(s) - 1:])]

def encrypt(plain_text, key):
    # Encrypt the plaintext
    cipher = AES.new(key.encode(), AES.MODE_ECB)
    return base64.b64encode(cipher.encrypt(pad(plain_text).encode()))

def decrypt(cipher_text, key):
    # Decrypt the ciphertext
    cipher = AES.new(key.encode(), AES.MODE_ECB)
    return unpad(cipher.decrypt(base64.b64decode(cipher_text)))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python filename.py <encrypt/decrypt> <value>")
        sys.exit(1)

    mode = sys.argv[1].lower()
    data = sys.argv[2]
    key = "Paste the obtained key from the application here"  # 16 characters for AES-128

    if mode == 'encrypt':
        encrypted_data = encrypt(data, key)
        print("Encrypted data (Base64 encoded):", encrypted_data.decode())
    elif mode == 'decrypt':
        decrypted_data = decrypt(data, key)
        print("Decrypted data:", decrypted_data.decode())
    else:
        print("Invalid mode. Please use 'encrypt' or 'decrypt'.")