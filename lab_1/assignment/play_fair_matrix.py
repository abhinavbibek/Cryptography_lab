def gen_key_mat(key):
    unique_key = ""
    for char in key:
        if char not in unique_key:
            unique_key += char
    alpha = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    comb = unique_key.upper()
    for c in alpha:
        if c not in comb:
            comb += c
    key_matrix = []
    for i in range(0, 25, 5):
        key_matrix.append(list(comb[i:i + 5]))
    return key_matrix

if __name__ == "__main__":
    key = "srmapuniversity"
    mat = gen_key_mat(key)
    print("Key Matrix:")
    for row in mat:
        print(" ".join(row))
