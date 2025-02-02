def gen_key_matrix(key):
    key = "".join(dict.fromkeys(key)) 
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  
    key_upper = key.upper()
    combined = ""
    for char in key_upper:
        if char not in combined:
            combined += char
    for char in alphabet:
        if char not in combined:
            combined += char
    matrix = []
    for i in range(0, len(combined), 5):
        matrix.append(list(combined[i:i + 5]))
    return matrix

def get_pos(matrix, char):
    for r, row in enumerate(matrix):
        if char in row:
            return r, row.index(char)

def enc_msg(msg, matrix):
    msg = msg.replace('J', 'I').upper()
    if len(msg) % 2 != 0:
        msg += 'X'
    cipher = ""
    for i in range(0, len(msg), 2):
        a, b = msg[i], msg[i + 1] 
        r1, c1 = get_pos(matrix, a)  
        r2, c2 = get_pos(matrix, b) 
        if r1 == r2:     #same row: shift right
            cipher += matrix[r1][(c1 + 1) % 5] + matrix[r2][(c2 + 1) % 5]
        elif c1 == c2:    #same column: shift down
            cipher += matrix[(r1 + 1) % 5][c1] + matrix[(r2 + 1) % 5][c2]
        else:      #rectangle rule: swap columns
            cipher += matrix[r1][c2] + matrix[r2][c1]
    return cipher

if __name__ == "__main__":
    key = "srmapuniversity"
    txt = "wearediscoveredsaveyourself"
    matrix = gen_key_matrix(key)
    print("Key Matrix:")
    for row in matrix:
        print(" ".join(row))
    cipher = enc_msg(txt, matrix)
    print("\nCipher Text:", cipher)
