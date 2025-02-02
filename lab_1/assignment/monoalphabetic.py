def encrypt(txt, key):
    enc_txt=""
    for char in txt:
        if char in key:
            enc_txt+=key[char]
        else:
            enc_txt+=char
    return enc_txt

def decrypt(txt, reverse_key):
    dec_txt=""
    for char in txt:
        if char in reverse_key:
            dec_txt+=reverse_key[char]
        else:
            dec_txt+=char
    return dec_txt

if __name__=="__main__":
    plain_txt="wewishtoreplaceplayer"
    key={
        'a':'q','b':'w','c':'e','d':'r','e':'t','f':'y','g':'u','h':'i',
        'i':'o','j':'p','k':'a','l':'s','m':'d','n':'f','o':'g','p':'h',
        'q':'j','r':'k','s':'l','t':'z','u':'x','v':'c','w':'v','x':'b',
        'y':'n','z':'m'
    }
    reverse_key={v:k for k,v in key.items()}
    cipher_txt=encrypt(plain_txt, key)
    print("Cipher Text:", cipher_txt)
    decrypted_txt=decrypt(cipher_txt, reverse_key)
    print("Decrypted Text:", decrypted_txt)
