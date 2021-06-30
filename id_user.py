a=["rolan123","dario456","pineres789"]
b=input("Enter the user: ")
c=input("Enter the ID: ")
print(b+c)
con=0
while True:
    if b+c in a:
        print("Welcome")
        break
    else:
        print("User or ID incorrect, try again: ")
        con+=1
        b=input("Enter the user: ")
        c=input("Enter the ID: ")   
        if con==3:
            print("User has been locked")
            False
            
            


