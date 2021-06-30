a=0
con=0
b=10
i=1
while con<10:
    con+=1
    print("----------------------------------")
    print(f"********TABLA DEL {con}*********")

    for i in range(b):
        a+=1
        print(con,"*",i+1,"=",con*(i+1))



   