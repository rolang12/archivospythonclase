import time

while True:
    
    print("1. Comenzar programa")
    print("2. Imprimir listado")
    print("3. Finalizar programa")
    us=int(input())
    if us>3 or us<1:
        print("Opción incorrecta, intentelo nuevamente")
        time.sleep(2)
        False
    if us==1:
        print("Opción 1")
        False
    if us==2:
        print("Opción 2")
        False
    if us==3:
        print("Opción 3")
        break
    