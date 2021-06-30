n=int(input("Ingrese el primer número: "))
m=int(input("Ingrese el segundo número: "))


if n % 2 ==0:
    n=n+1
elif m % 2 ==0:
    m -=1

while n<=m:
    print(n)
    n=n+2
    
