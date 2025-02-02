from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import os

def encrypt(msg, key):
    iv = os.urandom(8)  # generating a random IV
    cipher = DES.new(key, DES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(msg, DES.block_size))
    return iv, ciphertext

def decrypt(iv, ciphertext, key):
    cipher = DES.new(key, DES.MODE_CBC, iv)
    try:
        plaintext = unpad(cipher.decrypt(ciphertext), DES.block_size)
        return plaintext
    except ValueError:
        print("decryption failed, possible reasonns: incorrect key or corrupted file.")
        return None

def encrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as f:
        file_data = f.read()
    iv, encrypted_data = encrypt(file_data, key)
    print(f"generated IV: {iv.hex()}")
    if os.path.exists(output_file):
        os.remove(output_file)
    with open(output_file, 'wb') as f:
        f.write(iv + encrypted_data)
    print(f"file '{input_file}' encrypted and saved as '{output_file}'.")

def decrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as f:
        iv = f.read(8) 
        encrypted_data = f.read()
    print(f"iv read from file: {iv.hex()}")
    decrypted_data = decrypt(iv, encrypted_data, key)
    if decrypted_data is not None:
        with open(output_file, 'wb') as f:
            f.write(decrypted_data)
        print(f"File '{input_file}' decrypted and saved as '{output_file}'.")
    else:
        print("decryption failed.")

action = input("enter 'e' to encrypt a file or 'd' to decrypt a file: ").strip().lower()
file_path = "input.txt"
encrypt_path = "log_enc.txt"
decrypt_path = "log_dec.txt"
key = input("enter a key (8 chars): ").strip()
if len(key) != 8:
    print("key must be exactly 8 characters.")
else:
    key = key.encode('utf-8')  #converting key to bytes before using
    if action == 'e':
        encrypt_file(file_path, encrypt_path, key)
    elif action == 'd':
        decrypt_file(encrypt_path, decrypt_path, key)
    else:
        print("invalid option. please enter either e or d.")
