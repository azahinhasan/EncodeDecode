import codecs


def print_Code(x):
    
    output=''
    output=output.join(x)
    print("Result : " + output)
    main()


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
      
  


  x = list(input("Input the Value: "))
  options = input("Chose your Option (1: encode  or 2: decode) : ")
  if  options == '1':
      encode(x)
  elif  options == '2':
      decode(x)
  else:
        exit()


if __name__=="__main__": 
    main()




