n=int(input("Ingrese el primer número: "))
con=0
o=0
res=float
l=n
for i in range(n):
    o=o+1
    res=n%o
    
    if res==0:
        con+=1
        

    if l % 2 ==0:
      print(2)
      l=l/2
    elif l %5 ==0:
       print(5)
       l=l/5
    elif l%3==0:
        print(3)
        l=l/3
    elif l%11==0:
        print(11)
        l=l/11
    elif l%7==0:
        print(7)
        l=l/11
    elif l%13==0:
        print(13)
        l=l/13
   
'''
if con==2:
    print("El numero es primo")
else:
    print("El numero NO es primo")
    '''