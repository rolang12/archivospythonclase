# Elabora un programa para una discoteca que necesita controlar el acceso a las  personas
# la  cual pida el nombre a una persona y su edad, en caso  que  sea  mayor  de  18  lo deje
# ingresar, si es  menor  de edad debe  mostrar un  mensaje diciendole que no puede
# ingresar y si  tiene 18 años  debera  preguntar por su  identificación

nom=str(input("Ingrese el nombre: "))
ed=int(input("Ingrese su edad: "))

if ed>18:
    print(f"Bienvenid@ {nom}  ")
elif ed==18:
        print(f"Bienvenid@ {nom} ")
        dni=int(input('Ingrese su número de identificación para comprobar que es mayor de edad: '))
        print(dni)  
else :
    print(f"No puede ingresar (El acceso es solo para mayores de edad.) ")