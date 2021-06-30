
mensaje="INGRESE SU NOTA"
contar=0
total=0
grado = int(input(mensaje))



while grado != -1:
    
    if grado<-1:
        print("La nota debe ser positiva")
        
    total = total + grado
    contar += 1
    grado = int(input(mensaje))
    
else:
    
    if grado==0:
        print("No se ingresaron")
    else:
        promedio = total / contar
        print ("Promedio de notas del grado escolar: " + str(promedio))
   
