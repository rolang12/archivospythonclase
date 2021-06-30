'''Realiza un programa que imprima una secuencia de numeros de uno en uno desde el
que el usuario desee, el programa debe pedirle al usuario después de que imprima un
numero en pantalla le pregunte si desea continuar o no mostrando en pantalla'''




n=int(input("Ingrese el número de inicio: "))
c=True
while c==True:
    print(n)
   
    re=int(input("¿Desea seguir - [1 = Si / 2 = No]"))
    if re==2:
        c=False
    elif re==1:
        c=True
    elif re!=1 or re!=2:
        print("El número ingresado es incorrecto")
        c=False
    n+=1

'''Modificar el programa anterior para que sea una función que devuelva si el usuario
ingresó o no la contraseña correctamente, mediante un valor booleano (True o False).'''