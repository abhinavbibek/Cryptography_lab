from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad
import os
import socket


key = b"AIR12345SECUREKEY!"  #we can use 24 bytes for stronger security


# encrypts plaintext using 3DES with CBC mode
def encrypt(plaintext, key):
    plaintext = plaintext.encode('utf-8')  #convert to bytes
    iv = os.urandom(8)  
    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext, DES3.block_size))
    return iv + ciphertext  

# decrypts 3DES encrypted text
def decrypt(ciphertext, key):
    iv = ciphertext[:8]  
    ciphertext = ciphertext[8:]  #actual encrypted data
    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), DES3.block_size)
    return plaintext.decode('utf-8')  

# encrypting and sending a message over a socket connection
def send():
    s = socket.socket()
    host = socket.gethostname()
    port = 12345
    s.bind((host, port))
    s.listen(5)
    server_ip = socket.gethostbyname(host)
    print("\nlistening on IP:", server_ip)
    print('waiting for connection...')
    conn, addr = s.accept()
    print(f"\nconnection established with {addr[0]}:{addr[1]}\n")
    text = input("enter the plain text: ")
    encrypted_text = encrypt(text, key)
    print("encrypted message (hex):", encrypted_text.hex())
    conn.send(encrypted_text)
    print('message sent successfully\n')
    conn.close()


# receiving an encrypted message and decrypting it
def receive():
    s = socket.socket()
    host = "10.1.173.239"  #replace with sender's ip
    port = 12345
    s.connect((host, port))
    print('connected to sender')
    message = s.recv(1024)  #receive in bytes
    print("\nreceived encrypted message (hex):", message.hex())
    decrypted_message = decrypt(message, key)
    print("\ndecrypted message:", decrypted_message)
    s.close()

def main():
    while True:
        print("\n1 - Encrypt \n2 - Decrypt \n3 - Send \n4 - Receive \n5 - Stop")
        choice = input("enter your choice: ").strip()
        if choice == '1':
            text = input("enter the plain text: ")
            encrypted_text = encrypt(text, key)
            print("encrypted message (hex):", encrypted_text.hex())

        elif choice == '2':
            text = input("enter the encrypted text (hex): ")
            decrypted_text = decrypt(bytes.fromhex(text), key)
            print("decrypted message:", decrypted_text)

        elif choice == '3':
            send()

        elif choice == '4':
            receive()

        elif choice == '5':
            print("Stopping...")
            exit()

        else:
            print("invalid choice,enter a number from 1-5.")

if __name__ == "__main__":
    main()
