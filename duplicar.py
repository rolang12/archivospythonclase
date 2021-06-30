'''Dada la siguiente secuencia, hallar la expresión matemática para  realizar el  calculo de
tal forma que el  usuario  pueda  ingresar un numero y  la  calcule la secuencia hasta ese
numero ingresado1 2 4 8 16 32 64 128 256 512 1024 2048 ......si el  usuario  ingresa 200
debe mostrar la  secuencia  así,  1 2 4 8 16 32 64 128'''

a=int(input("Ingrese el número límite"))
con=0
n=1
m=0
f=0
t=0
while t<a:
   
    con+=1
    n=n*2
    t=n

    if t>a:
        break
    else:
        print(t)
    
