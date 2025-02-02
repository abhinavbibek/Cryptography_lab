def encrypt(ip_txt, key):
    encrypt_txt= ""
    for char in ip_txt:
        if 'a' <= char <= 'z':
            encrypt_char = chr(((ord(char) - ord('a') + key) % 26) + ord('a'))
        elif 'A' <= char <= 'Z':
            encrypt_char = chr(((ord(char) - ord('A') + key) % 26) + ord('A'))
        else:
            encrypt_char = char
        encrypt_txt+= encrypt_char
    return encrypt_txt

if __name__ == "__main__":
    plain_txt = input("Enter the text to encrypt: ")
    key = 4 
    cipher_txt = encrypt(plain_txt, key)
    print("Encrypted Text:", cipher_txt)