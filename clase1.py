'''
n1=int(input("INGRESE UN NUMERO"))
n2=int(input("INGRESE UN NUMERO"))
n3=int(input("INGRESE UN NUMERO"))
n4=int(input("INGRESE UN NUMERO"))
n5=int(input("INGRESE UN NUMERO"))
may=max(n1, n2, n3, n4, n5)
prom=(n1+n2+n3+n4+n5)/5
print(f"El número mayor es : {may} y el promedio es {prom}")
'''
may=0
n=int(input("INGRESE UN NUMERO"))
i=0
print("------------------------")
for i in range(n):
    nu=int(input("INGRESE UN NUMERO"))
    if nu>may:
        may=nu

print(may)

