def enc(txt, key):
    res = ""
    key = key.lower()
    k_len = len(key)
    k_idx = 0
    for ch in txt:
        if 'a' <= ch <= 'z':
            shift = ord(key[k_idx]) - ord('a')
            res += chr(((ord(ch) - ord('a') + shift) % 26) + ord('a'))
            k_idx = (k_idx + 1) % k_len
        elif 'A' <= ch <= 'Z':
            shift = ord(key[k_idx]) - ord('a')
            res += chr(((ord(ch) - ord('A') + shift) % 26) + ord('A'))
            k_idx = (k_idx + 1) % k_len
        else:
            res += ch
    return res

def dec(txt, key):
    res = ""
    key = key.lower()
    k_len = len(key)
    k_idx = 0
    for ch in txt:
        if 'a' <= ch <= 'z':
            shift = ord(key[k_idx]) - ord('a')
            res += chr(((ord(ch) - ord('a') - shift) % 26) + ord('a'))
            k_idx = (k_idx + 1) % k_len
        elif 'A' <= ch <= 'Z':
            shift = ord(key[k_idx]) - ord('a')
            res += chr(((ord(ch) - ord('A') - shift) % 26) + ord('A'))
            k_idx = (k_idx + 1) % k_len
        else:
            res += ch
    return res

if __name__ == "__main__":
    plain = "wearediscoveredsaveyourself"
    key = "deceptive"
    cipher = enc(plain, key)
    print("Cipher Text:", cipher)
    dec_txt = dec(cipher, key)
    print("Decrypted Text:", dec_txt)
