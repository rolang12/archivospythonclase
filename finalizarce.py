'''Realice un programa que acumule todo numero  ingresado  por  el  usuario, el  programa
deberá  finalizar cuando el  usuario ingrese el numero 0,  el  programa  al final  debe
mostrar cual  es el numero acumulado'''

cont=0
c=0
a=0
b=0
while b!=0 or a==0:
    cont+=1
    b=int(input("Ingrese el número: "))
    c=c+b
    if b==0:
        break

print ("El acumulado es: ",c," -  Y la cantidad de números ingresados es: ",cont)




