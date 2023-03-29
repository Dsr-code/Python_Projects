a= open("password.txt","r")
print("inside file")
for i in a:
    if i == "d" :
        print("match found \n")
        print("your password is d")
        break
