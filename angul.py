'''Un ángulo se considera agudo si es menor de 90 grados, obtuso si es mayor de 90
grados y recto si es igual a 90 grados. Utilizando esta información, escribir un algoritmo
que acepte un ángulo en grados y visualice el tipo de ángulo correspondiente a los
grados introducidos'''

ang=float(input("Digite el valor del ángulo: "))

if ang<90:
    print("El angulo es agudo")
elif ang>90:
    print("El angulo es obtuso")
elif ang==90:
    print("El angulo es recto")