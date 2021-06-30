# n1=int(input("INGRESE UN NUMERO"))
# n2=int(input("INGRESE UN NUMERO"))
# n3=int(input("INGRESE UN NUMERO"))

# may=max(n1, n2, n3)
# men=min(n1, n2, n3)

# med=(n1+n2+n3)-may-men

# print(may)
# print(med)
# print(men)

print('Digite tres números de manera seguida separados por un espacio: ',end=" ")
numeros=list(map(int, input().split() ))

print(f" los numeros ingresados son:{numeros} " )

numeros.sort()
print("-------------------")
numeros.reverse()

print(f" Organizados de forma Descendente son {numeros}")