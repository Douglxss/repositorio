dia = int(input("INGRESE EL DIA "))
mes = int(input("INGRESE EL MES "))
anhio = int(input("INGRESE EL AÑO "))

if anhio > 0 and mes > 0 and mes <= 12:
    if mes in (1, 3, 5, 7, 8, 10, 12):
        if 1 <= dia <= 31:
            print("LA FECHA ES CORRECTA")
        else:
            print("FECHA INCORRECTA, INGRESE UNA FECHA CORRECTA")
    elif mes in (4, 6, 9, 11):
        if 1 <= dia <= 30:
            print("LA FECHA ES CORRECTA")
        else:
            print("FECHA INCORRECTA, INGRESE UNA FECHA CORRECTA")
    elif mes == 2:
        if 1 <= dia <= 28:
            print("LA FECHA ES CORRECTA")
        elif anhio % 4 == 0 and anhio % 100 != 0 or anhio % 400 == 0:
            if 1 <= dia <= 29:
                print("LA FECHA ES CORRECTA")
        else:
            print("FECHA INCORRECTA, INGRESE UNA FECHA CORRECTA")