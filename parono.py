# n1=int(input("INGRESE UN NUMERO"))

# if n1 % 2 ==0:
#     print(f"El numero {n1} es par")
# else:
#     print(f"El numero {n1} es impar")
n = 15
for x in range(1, 15):
    if x % 3 == 0 and x % 5 == 0:
        print("SoloLearn")
    elif x % 2 == 0:
        continue 
    elif x % 3 == 0:
        print("Solo")       
    elif x % 5 == 0:
        print("Learn")
    else:
        print(x)

#1, SOLO LEARN 7 SOLO 11 13