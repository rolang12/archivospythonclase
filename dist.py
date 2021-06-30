# Construye un programa que Si distancia es mayor que 20 y menos que 35, leer un valor
# para tiempo y calcular  la  Velocidad si   Distancia = Velocidad * Tiempo

di=int(input("Digite el valor de la distancia"))

if di>20 and di<35:
    ti=int(input("Digite un valor para el tiempo"))
    print(f"El valor de la distancia es {di*ti}")