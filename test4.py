import codecs


def print_Code(x):
    
    output=''
    output=output.join(x)
    print(output)


def encode(x):
  for i in range(len(x)):
    a = ord(x[i])
    a=a+2
    x[i]=chr(a)
  
  print_Code(x)

def decode(x):
  for i in range(len(x)):
    a = ord(x[i])
    a=a-2
    x[i]=chr(a)
  
  print_Code(x)




##hex = ord('Z')
##print(hex)

##hex = hex;

####text =  chr(hex)
##print(text)



def main():
      
print("Chose your Option (1: encode  or 2: decode):"
input = input()


  x = list(input())
  if  input == 1:
      encode(x)
  elif  input == 2:
      decode(x)
  else:
        exit()


if __name__=="__main__": 
    main()




