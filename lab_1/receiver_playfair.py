import socket 

def create_matrix(key):  # creating playfair matrix
 key="".join(dict.fromkeys(key.upper().replace("J","I")))  
 alphabet="ABCDEFGHIKLMNOPQRSTUVWXYZ"
 matrix=[char for char in key if char.isalpha()]+[char for char in alphabet if char not in key]
 return [matrix[i:i+5] for i in range(0,25,5)]

def decrypt_pair(pair,matrix):
 positions={char:(row,col) for row,row_values in enumerate(matrix) for col,char in enumerate(row_values)}
 r1,c1=positions[pair[0]]
 r2,c2=positions[pair[1]]
 if r1==r2: 
     return matrix[r1][(c1-1)%5]+matrix[r2][(c2-1)%5]  # same row
 elif c1==c2: 
     return matrix[(r1-1)%5][c1]+matrix[(r2-1)%5][c2]  # same column
 else: 
     return matrix[r1][c2]+matrix[r2][c1]  # rectangle

def playfair_decrypt(encrypted_text,key): 
 matrix=create_matrix(key)
 decrypted_text=""
 for i in range(0,len(encrypted_text),2):
  decrypted_text+=decrypt_pair(encrypted_text[i:i+2],matrix)
 return decrypted_text.rstrip("X")  # remove padding

key="SECRET"  # shared key
sock=socket.socket()
host=input("\nenter sender ip: ").strip()
port=12345
sock.connect((host,port))
print('connected')
while True:
 encrypted_message=sock.recv(1024).decode('utf-8').strip()
 if encrypted_message=="EXIT":
  print("\nsender closed connection. exiting...")
  break
 if encrypted_message:
  print("\nencrypted received:",encrypted_message)
  decrypted_message=playfair_decrypt(encrypted_message,key) 
  print("decrypted:",decrypted_message)
 else: print("\nno message received or empty.")
sock.close()
