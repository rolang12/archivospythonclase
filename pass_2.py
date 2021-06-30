'''Escribir un programa que contenga una contraseña inventada, que le pregunte al usuario
la contraseña, y no le permita continuar hasta que la haya ingresado correctamente.'''

pas=123456
a=False

while a==False:
    a=int(input("Digite la contraseña"))
    if a!=pas: 
      a=False
    else:
      a=True