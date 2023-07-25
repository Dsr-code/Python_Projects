import random
import string

sign = input("Enter 0 to encrypt and 1 to decrypt : \n")
message = input("Enter your message : \n")

msglst = message.split(" ")
# print(msglst)


# cyphermsg = ""
encryption = True if (sign=="0")else False
if (encryption==True):
    newword = []
    for word in msglst:
        # print(word)
        if len(word)>=3:
            messageN=word[1:]+word[0]
            ran="".join(random.choices(string.ascii_lowercase+string.digits+string.punctuation, k=6))
            mixedword=(ran[0:3]+messageN+ran[3:6])
            # print(mixedword)
            newword.append(mixedword)
            
        else:
            newword.append(word[::-1])
    
    print("\n\n The encrypted message : ")        
    print(" ".join(newword))
    
else:
    newword=[]
    for word in msglst:
        # print(word)
        if len(word)>=3:
            messageN=word[3:-3]
            messageN=messageN[-1]+messageN[:-1]
            
            # print(mixedword)
            newword.append(messageN)
            
        else:
            newword.append(word[::-1])
            
    print("\n\n The decrypted message : ")        
    print(" ".join(newword))
        
            
            
            
            