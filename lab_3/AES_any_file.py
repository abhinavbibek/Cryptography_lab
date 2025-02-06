from cryptography.fernet import Fernet
import os

def generate_key():
    if not os.path.exists("secret.key"):
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
    else:
        key = load_key()
    return key

def load_key():
    with open("secret.key", "rb") as key_file:
        return key_file.read()

def encrypt_file(input_file):
    key = generate_key()
    cipher = Fernet(key)
    with open(input_file, 'rb') as f:
        data = f.read()
    enc_data = cipher.encrypt(data)
    output_file = input_file + ".encrypted"
    with open(output_file, 'wb') as f:
        f.write(enc_data)
    print(f"encrypted file saved as {output_file}")

def decrypt_file(input_file):
    key = load_key()
    cipher = Fernet(key)
    with open(input_file, 'rb') as f:
        enc_data = f.read()
    data = cipher.decrypt(enc_data)
    output_file = input_file.replace(".encrypted", "")
    decrypted_output_file = output_file + ".decrypted"
    with open(decrypted_output_file, "wb") as f:
        f.write(data)
    print(f"decrypted file saved as {decrypted_output_file}")

def main():
    while True:
        print("1 - encrypt file\n2 - decrypt file\n3 - exit")
        choice = input("enter choice: ")
        if choice == "1":
            input_file = input("enter file to encrypt: ")
            encrypt_file(input_file)
        elif choice == "2":
            input_file = input("enter file to decrypt: ")
            decrypt_file(input_file)
        elif choice == "3":
            print("bye!")
            break
        else:
            print("invalid i/p")

if __name__ == "__main__":
    main()
