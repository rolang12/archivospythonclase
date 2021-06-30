anio=int(input("Ingrese el año: "))
mes=int(input("Ingrese el número del mes: "))

if mes==1:
    print("1. Enero tiene 31 días")
elif mes==2:
    if anio %4==0:
        print("2 Febrero tiene 29 días")
    else:
        print("2 Febrero tiene 28 días")
elif mes==3:
    print("3. Marzo tiene 31 días")
elif mes==4:
    print("4. Abril tiene 30 días")
elif mes==5:
    print("5. Mayo tiene 31 días")
elif mes==6:
    print("6. Junio tiene 30 días")
elif mes==7:
    print("7. Julio tiene 31 días")
elif mes==8:
    print("8. Agosto tiene 31 días")
elif mes==9:
    print("9. Septiembre tiene 30 días")
elif mes==10:
    print("10. Octubre tiene 31 días")
elif mes==11:
    print("11. Noviembre tiene 30 días")
elif mes==12:
    print("12. Diciembre tiene 31 días")
else:
    print("Valor incorrecto")


