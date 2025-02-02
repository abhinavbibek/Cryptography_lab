import socket  # importing socket module

def create_matrix(key):  # create playfair matrix
 key="".join(dict.fromkeys(key.upper().replace("J","I")))  
 alphabet="ABCDEFGHIKLMNOPQRSTUVWXYZ"
 matrix=[char for char in key if char.isalpha()]+[char for char in alphabet if char not in key]
 return [matrix[i:i+5] for i in range(0,25,5)]

def encrypt_pair(pair,matrix):  # playfair encrypt pair
 positions={char:(row,col) for row,row_values in enumerate(matrix) for col,char in enumerate(row_values)}
 r1,c1=positions[pair[0]]
 r2,c2=positions[pair[1]]
 if r1==r2: 
     return matrix[r1][(c1+1)%5]+matrix[r2][(c2+1)%5]  # same row
 elif c1==c2: 
     return matrix[(r1+1)%5][c1]+matrix[(r2+1)%5][c2]  # same column
 else: 
     return matrix[r1][c2]+matrix[r2][c1]  # rectangle

def playfair_encrypt(message,key): 
 matrix=create_matrix(key)
 message=message.upper().replace("J","I").replace(" ","")
 message="".join([message[i]+"X" if i+1<len(message) and message[i]==message[i+1] else message[i] for i in range(len(message))])
 if len(message)%2:
  message+="X" 
 encrypted_text=""
 for i in range(0,len(message),2):
  encrypted_text+=encrypt_pair(message[i:i+2],matrix)
 return encrypted_text

key="SECRET"  # shared key
sock=socket.socket()
host=socket.gethostname()
port=12345
sock.bind((host,port))
sock.listen(5)
server_ip=socket.gethostbyname(host)
print(f"\nListening on IP: {server_ip}")
print('Waiting for connection...')
conn,addr=sock.accept()
print(f"\nConnection established with {addr[0]} : {addr[1]}")
while True:
 message=input("\nEnter the message to send (type 'exit' to quit): ").strip()
 if message.lower()=="exit":
  print("Closing connection...")
  conn.sendall("EXIT".encode('utf-8'))
  break
 if message:
  encrypted_message=playfair_encrypt(message,key)
  print("Encrypted message:",encrypted_message)
  conn.sendall(encrypted_message.encode('utf-8'))
  print("Message sent successfully.")
 else:
  print("No message entered. Please type a valid message.")
conn.close()
