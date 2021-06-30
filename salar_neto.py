hor=int(input("Ingrese el número de horas trabajadas: "))
tar=int(input("Ingrese la tarifa: "))



        
if hor<=35:
    su1=hor*tar
    nom=str(input("Ingrese el nombre: "))
    
    if su1<=2000:   
      su1=2000
    elif su1>2000 and su1<2221:
        su1=su1*20/100
    elif su1>2220:
        su1=su1*30/100
    print(f"El salario neto de {nom} es de: {su1}$")
if hor>35:
    su1=35*tar
    nom=str(input("Ingrese el nombre: "))

    su2=hor-35
    su2f=su2*tar*1.5
    salf=su2f+su1

    if salf<=2000:   
      salf=2000
    elif salf>2000 and salf<2221:
        salf=salf*20/100
    elif salf>2220:
        salf=salf*30/100
        print(f"El salario neto para  {nom} es de  {salf}$ ")

