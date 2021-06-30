import os
os.system('cls')

n1=int(input("INGRESE UN NUMERO: "))
n2=int(input("INGRESE UN NUMERO: "))
n3=int(input("INGRESE UN NUMERO: "))

n=min(n1, n2, n3)

if n1>n2 and n1<n3:
    med=n1
elif n1<n2 and n1>n3:
    med=n1
elif n2>n1 and n2<n3:
    med=n2
elif n2<n1 and n2>n3:
    med=n2
elif n3>n1 and n3<n2:
    med=n3
elif n3<n1 and n3>n2:
    med=n3

print(f" El número intermedio es {med} ")