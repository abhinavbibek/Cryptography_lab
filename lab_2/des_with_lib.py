from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import os

def encrypt(msg , key): 
    # creating a des cipher object
    cipher = DES.new(key.encode('ascii') , DES.MODE_CBC)  
    # encrypting the message with padding
    ciphertext = cipher.encrypt(pad(msg.encode('ascii') , DES.block_size))
    return cipher.iv , ciphertext  # returning iv and ciphertext

def decrypt(iv , ciphertext , key): 
    cipher = DES.new(key.encode('ascii') , DES.MODE_CBC , iv)  
    try:
        # decrypting and unpadding the message
        plaintext = unpad(cipher.decrypt(ciphertext) , DES.block_size)
        return plaintext.decode('ascii') 
    except ValueError:  
        return False  # returning False if unpadding fails

user_input = input('enter a message (8 chars): ')
key = input('enter a key (8 chars): ')  # taking key as a string

# checking if the key is exactly 8 bytes long
if len(key) != 8: 
    print("key must be exactly 8 characters.")
else:
    iv , ciphertext = encrypt(user_input , key) 
    print(f'cipher text: {ciphertext}')  # printing ciphertext as bytes
    plaintext = decrypt(iv , ciphertext , key)  
    print(f'Plain text: {plaintext}') 
