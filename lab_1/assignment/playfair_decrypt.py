def gen_key_mat(key):
    unique_key = ""
    for char in key:
        if char not in unique_key:
            unique_key += char
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  
    combined = unique_key.upper()    #building the combined character set
    for char in alphabet:
        if char not in combined:
            combined += char
    key_matrix = []
    for i in range(0, 25, 5):
        key_matrix.append(list(combined[i:i + 5]))
    return key_matrix

def get_pos(mat, char):
    for r in range(len(mat)):
        for c in range(len(mat[r])):
            if mat[r][c] == char:
                return r, c
    return None  

def dec_msg(cipher, mat):
    plain = ""
    for i in range(0, len(cipher), 2):
        a, b = cipher[i], cipher[i + 1]
        r1, c1 = get_pos(mat, a)
        r2, c2 = get_pos(mat, b)
        if r1 == r2:  
            plain += mat[r1][(c1 - 1) % 5] + mat[r2][(c2 - 1) % 5]
        elif c1 == c2: 
            plain += mat[(r1 - 1) % 5][c1] + mat[(r2 - 1) % 5][c2]
        else:  
            plain += mat[r1][c2] + mat[r2][c1]
    return plain

if __name__ == "__main__":
    key = "srmapuniversity"
    cipher = "LIIUDLTQNSLIZETQVTPKZEZFVBVZ"
    mat = gen_key_mat(key)
    print("Key Matrix:")
    for row in mat:
        print(" ".join(row))
    plain_msg = dec_msg(cipher, mat)
    print("\nDecrypted Message:", plain_msg)
