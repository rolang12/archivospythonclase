n=int(input("Ingrese el número: "))
 
o=0
con=0
i=0
t=0
while o!=n:
    o=o+1
    t=0
    con=0
    for i in range(o):
        t+=1
        res=o%t
        
        if o==1:
         con=0
        if res==0:
            con=con+1
    if con==2:
        print(o)
        con=0
        
    
    
            
    


               
                
             

