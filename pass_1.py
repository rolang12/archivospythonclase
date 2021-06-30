'''Escribir un programa que contenga una contraseña inventada, que le pregunte al usuario
la contraseña, y no le permita continuar hasta que la haya ingresado correctamente. 
SOLO CON 3 INTENTOS'''
import time
pas=123456
a=False
i=0
n=0

while a==False and i!=3:
    i+=1
    a=int(input("Digite la contraseña"))
    if a!=pas: 
        print("Incorrect Password, try again!")
        n+=1
        a=False
        time.sleep(n)
    else:
      a=True

