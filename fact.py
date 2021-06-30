n=int(input("Ingrese el número límite: "))
t=0
m=n
l=m
while t<n-1:
    t+=1
    m=(l-1)*m
    l-=1
    
print("------------------")

print(m)
