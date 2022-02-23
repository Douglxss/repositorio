temperatura = int(input("Ingrese la temperatura:"))

if temperatura < 0:
    print("Es solida")

elif temperatura >= 0 and temperatura <= 100 :
    print("Es liquida")

elif temperatura > 100:
    print("Es gaseosa")
