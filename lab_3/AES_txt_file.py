from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    return key

def load_key():
    with open("secret.key", "rb") as key_file:
        return key_file.read()

def encrypt_file(input_file, output_file):
    key = generate_key()
    cipher = Fernet(key)
    with open(input_file, 'rb') as f:
        data = f.read()
    enc_data = cipher.encrypt(data)
    with open(output_file, 'wb') as f:
        f.write(enc_data)
    print(f"decrypted file saved as {output_file}")

def decrypt_file(input_file, output_file):
    key = load_key()
    cipher = Fernet(key)
    with open(input_file, 'rb') as f:
        enc_data = f.read()
    data = cipher.decrypt(enc_data)
    with open(output_file, "wb") as f:
        f.write(data)
    print(f"encrypted file saved as {output_file}")

def main():
    while True:
        print("1 - encrypt file\n2 - decrypt file\n3 - exit")
        choice = input("enter choice: ")
        if choice == "1":
            input_file = input("enter file to encrypt: ")
            encrypt_file(input_file, "encrypted_file.txt")
        elif choice == "2":
            decrypt_file("encrypted_file.txt", "decrypted_file.txt")
        elif choice == "3":
            print("bye!")
            break
        else:
            print("invalid i/p")

if __name__ == "__main__":
    main()
