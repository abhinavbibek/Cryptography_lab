key = "AIR"

def encrypt(text,key):
    text = text.lower().replace(" ","")
    key = key.lower().replace(" ","")
    textt = list(text)
    keyy = list(key)

    if len(keyy) < len(textt):  #Making plain text and key equal length by embeding at last
        for ch in keyy:
            if (len(keyy) != len(textt)):
                keyy.append(ch)
            else:
                break
    
    cip_text = ''

    for a,b in zip(textt, keyy):
        ch = chr(((ord(b)-ord('a')) + (ord(a)-ord('a'))) %26 + ord('a'))    # Dealing with ord(a) as ascii of 'a' is not the start
        cip_text += ch.upper()                                              # Many chars are there before that

    print("Cipher text : ", cip_text)

    return cip_text
    


def decrypt(text, key):
    text = text.lower().replace(" ","")
    key = key.lower().replace(" ","")
    textt = list(text)
    keyy = list(key)

    if len(keyy) < len(textt):  #Making plain text and key equal length by embeding at last
        for ch in keyy:
            if (len(keyy) != len(textt)):
                keyy.append(ch)
            else:
                break
    
    plain_text = ''

    for a,b in zip(textt,keyy):
        ch = chr(((((ord(a)-ord('a')) - (ord(b)-ord('a'))) +26) %26) + ord('a'))
        plain_text += ch

    print("Plain text : ",plain_text.upper())
    plain_textt = plain_text.upper()
    return plain_textt


def send():
    import socket

    # Create socket
    s = socket.socket()
    host = socket.gethostname()
    port = 12345

    s.bind((host, port))
    s.listen(5)

    server_ip = socket.gethostbyname(host)
    print("\nListening to ip:", server_ip)
    print('Waiting for connection...')

    conn, addr = s.accept()
    print(f"\nConnection established with {addr[0]} : {addr[1]}\n")


    text = input("Enter the plain text : ")
    encrypted_text = encrypt(text,key)
    print("\n\t", encrypted_text)
    # Get text input from user
    # message = input("Enter your message to send: ")

    # Send the message
    conn.send(encrypted_text.encode())
    print('Message sent successfully\n')

    conn.close()


def receive():

    import socket

    # Create socket
    s = socket.socket()
    host = "10.1.173.239"  # Replace with sender's IP
    port = 12345

    s.connect((host, port))
    print('Connected to sender')

    # Receive the message
    message = s.recv(1024).decode()
    print("\n\t",message)
    decrypt_message = decrypt(message,key)    
    print("\nReceived message:", decrypt_message)

    s.close()



def main():
    while True:
        print("\n1 - Encrypt \n2 - Decrypt \n3 - Send \n4 - Receive \n5 - Stop")
        choice = int(input("Enter the choice : "))

        if choice == 1:
            # text = input("Enter the plain text : ")
            # key = input("Enter the key : ")
            # encrypt(text,key)
            print("hii")

        elif choice == 2:
            # text = input("Enter the Cipher text : ")
            # key = input("Enter the key : ")
            # decrypt(text,key)
            print("HIII")

        elif choice == 3:
            send()
        
        elif choice == 4:
            receive()
        elif choice == 5 :
            print("Stopping the server .....")
            exit()

        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()