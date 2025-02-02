def decrypt(txt, key):
    reverse_key = {}
    for k, v in key.items():
        reverse_key[v] = k
    dec_txt = ""
    for char in txt:
        if char in reverse_key:
            dec_txt += reverse_key[char]  #substitute encrypted character
        else:
            dec_txt += char  #keep characters that aren't in key
    return dec_txt


if __name__ == "__main__":
    cipher_txt = "SEEMSEAOMEDSAMHL"
    key = {
        'A': 'A', 'B': 'N', 'C': 'D', 'D': 'R', 'E': 'E', 'F': 'W', 'G': 'I', 'H': 'C',
        'I': 'K', 'J': 'S', 'K': 'O', 'L': 'H', 'M': 'T', 'N': 'B', 'O': 'F', 'P': 'G',
        'Q': 'J', 'R': 'L', 'S': 'M', 'T': 'P', 'U': 'Q', 'V': 'U', 'W': 'V', 'X': 'X',
        'Y': 'Y', 'Z': 'Z'
    }
    plain_txt = decrypt(cipher_txt, key)
    print("Plain Text:", plain_txt)
