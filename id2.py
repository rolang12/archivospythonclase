list_admi = []
num_usu = int(input("Ingrese la cantidad de usuarios a guardar en la lista"))
for _ in range(num_usu):
    di = int(input("Ingrese su numero de ID: "))
    clave = int(input("Ingrese su clave"))
    usu = di,clave
    list_admi.append(usu)
print (list_admi)
x = 0
while x <= 3:
    d = int(input("Ingrese su ID "))
    c = int(input("Ingrese su clave"))
    usu2 = d,c
    if usu2 in list_admi:
        print("Bienvenido")
        break
    else:
        print("Usuario incorrecto, Digite bien su ID y clave")
        x -= 1
            