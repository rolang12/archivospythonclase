
uno=0
dos=0
tres=0
cua=0
cont=0

num=int(input("Cuántas personas desean registrar su peso?"))

while cont <= num-1:
  pes=float(input("¿Cuál es su peso?"))
  cont+=1
  if pes<=40:
      uno +=1
  elif pes> 40 and pes <=50:
      dos +=1
  elif pes>50 and pes <=60:
      tres+=1
  elif pes>60:
      cua +=1


print(f"El total de personas cuyo peso es menor a 40 es: {uno} ")
print(f"El total de personas cuyo peso es mayor a 40 y menor que 50 es: {dos} ")
print(f"El total de personas cuyo peso es mayor a 50 y menor a 60 es: {tres} ")
print(f"El total de personas cuyo peso es mayor a 60 es: {cua} ")




