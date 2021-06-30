import random
n=random.randint(1,10)
print(n)

n1=0

while n1!=n:
    n1=int(input("Ingrese el número: "))
    if n1<n:
        print("El numero que ingresó es menor al que está adivinando")
    elif n1==n:
        print("Ha encontrado el número")
        n1=n
    else:
        print("El numero que ingresó es mayor al que está adivinando")