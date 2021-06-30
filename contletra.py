'''El usuario ingresa por teclado una oración por ejemplo 'Las cuentas claras y el chocolate
espeso' el programa debe permitir buscar la  letra que el usuario quiere buscar y contar
cuantas letras hay; Ejemplo: letra a buscar 's'; 'Las cuentas claras y el chocolate
espeso' posee 4 letras 's'''

ora=input("Ingrese la oración: ")

bus=str(input("Ingrese la letra que desea buscar: "))
con=0
for i in ora:
    if i==bus:
        con+=1

print(f"La letra: {bus} está: {con} veces  ")


