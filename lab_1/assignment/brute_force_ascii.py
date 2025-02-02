def encrypt(message, shift):
    result = ""
    for ch in message:
        if 'a' <= ch <= 'z':
            result += chr(((ord(ch) - ord('a') + shift) % 26) + ord('a'))
        elif 'A' <= ch <= 'Z':
            result += chr(((ord(ch) - ord('A') + shift) % 26) + ord('A'))
        else:
            result += ch  #keep non-alphabet characters as it is
    return result


def decrypt(cipher_text, shift):
    result = ""
    for ch in cipher_text:
        if 'a' <= ch <= 'z':
            result += chr(((ord(ch) - ord('a') - shift) % 26) + ord('a'))
        elif 'A' <= ch <= 'Z':
            result += chr(((ord(ch) - ord('A') - shift) % 26) + ord('A'))
        else:
            result += ch
    return result


def brute_force(cipher_text):
    print("\nTrying all possible shifts:")
    for key in range(1, 26):
        print(f"Key {key}: {decrypt(cipher_text, key)}")


if __name__ == "__main__":
    encrypted_sample = "PHHW PH DIWHU WKH WRJD SDUWB"
    brute_force(encrypted_sample)
