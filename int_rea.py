
n=(input("Ingrese un número".split()))
print(n)
print(type(n))
# i=0
# cont=0
# for i in range(len(n.split())):
    
#     if n==".":
#        print("El numero es real")
#     else:
#        print("El numero es entero")

cont=0
indice = 0
while indice < len(n):
    letra = n[indice]
    print (letra)
    if letra==".":
        cont=3    
    indice += 1


if cont==3:
    print("El numero es real")
elif cont==0:
    print("El numero es entero")