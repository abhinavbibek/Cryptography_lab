def check( path ):  
 with open( path , 'r' ) as file :  
  content = file.read( )  
  words = content.split( )  
  word_c=len( words )  
  char_c = len( content.replace( " ","" ) )  
  print( f"Word Count:{word_c}" )  
  print( f"Character Count (excl. spaces):{char_c}" )  
  print( "\nASCII Values of Characters:" )  
  
  for char in content :  
   if char !=" " :   
    print( f"'{char}': {ord(char)}" )  
  
if __name__ == "__main__" :  
 path=r'C:\Users\bibek\Desktop\cryptography\lab_1\assignment\log.txt'  
 check( path )  
