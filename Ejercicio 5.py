

#Entrada
num1 = int(input("Ingrese primer numero"))
num2 = int(input("Ingrese segundo numero"))
num3 = int(input("Ingrese tercer numero"))
#Salida
if num1>num2 and num1>num3:
    print("el numero mayor es:", num1)

elif num2>num1 and num2>num3:
    print("el numero mayor es:", num2)

elif num1==num2 and num1==num3 and num2==num3 :
    print("Todos los numeros son iguales")

elif num3>num1 and num3>num2:
    print("el numero mayor es:", num3)

elif num1==num2:
    print("El primer y segundo numero son iguales")

elif num1==num3:
    print("El primer y tercer numero son iguales")

elif num2==num3:
    print("El segundo y tercer numero son iguales")

