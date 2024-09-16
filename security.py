from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

key = os.environ.get('ENCRYPTION_KEY') or b'encryption_key_32_bytes'

def encrypt_data(plain_text):
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    return iv + encryptor.update(plain_text.encode()) + encryptor.finalize()

def decrypt_data(cipher_text):
    iv = cipher_text[:16]
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    return decryptor.update(cipher_text[16:]) + decryptor.finalize()
