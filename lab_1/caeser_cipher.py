def ce(t,s):   
 r=""   
 for c in t:  
  if c.isalpha():  
   sa = s % 26  
   nc = chr(((ord(c.lower()) - ord('a') + sa) % 26) + ord('a'))
   r+= nc.upper() if c.isupper() else nc
  else: r+=c
 return r

def cd(t,s): 
    return ce(t,-s)  # decryption by reversing shift

def snd():
 import socket  
 s=socket.socket() 
 h=socket.gethostname()
 p=12345
 s.bind((h,p))
 s.listen(5)
 ip=socket.gethostbyname(h)
 print("\nlistening to ip:",ip)
 print('waiting for connection...')
 c,a=s.accept()
 print(f"\nconnection with {a[0]}:{a[1]}\n")
 txt=input("enter text: ")
 sh=int(input("enter shift: "))
 et=ce(txt,sh)
 print("\nencrypted:",et)
 c.send(et.encode())
 print('message sent\n')
 c.close()

def rcv():
 import socket
 s=socket.socket()
 h="10.1.173.239"  #sender ip
 p=12345
 s.connect((h,p))
 print('connected')
 msg=s.recv(1024).decode()
 print("\nreceived encrypted:",msg)
 sh=int(input("enter shift to decrypt: "))
 dmsg=cd(msg,sh)
 print("\ndecrypted:",dmsg)
 s.close()

def main():
 while 1: 
  print("\n1-encrypt 2-decrypt 3-send 4-receive 5-stop")
  ch=int(input("choice: "))
  if ch==1:
   txt=input("text: ")
   sh=int(input("shift: "))
   print("encrypted:",ce(txt,sh))
  elif ch==2:
   txt=input("encrypted text: ")
   sh=int(input("shift: "))
   print("decrypted:",cd(txt,sh))
  elif ch==3: snd()
  elif ch==4: rcv()
  elif ch==5:
   print("stopping...")
   exit()
  else: print("invalid")

if __name__=="__main__":
    main()
