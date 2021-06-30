ora=input("Ingrese la oración: ")


con=0
con2=0
con3=0
con4=0
con5=0

for i in ora:
    if i=="a" or i=="A":
        con+=1
    if i=="e" or i=="E":
        con2+=1
    if i=="i" or i=="I":
        con3+=1
    if i=="o" or i=="O":
        con4+=1
    if i=="u" or i=="U":
        con5+=1


print(f"La letra: [A] está: {con} veces  ")
print(f"La letra: [E] está: {con2} veces  ")
print(f"La letra: [I] está: {con3} veces  ")
print(f"La letra: [O] está: {con4} veces  ")
print(f"La letra: [U] está: {con5} veces  ")


