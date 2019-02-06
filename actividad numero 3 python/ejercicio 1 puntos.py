print("1.opcion 2.opcion".center(81,"*"))
opcion = input (":.")

if opcion == "1":
    numero1 = input("ingrese primer numero")
    numero2 = input("ingrese a que numero quiere elevarlo")
    elevacion = int(numero1) ** int(numero2)
    print("la levacion es:. {}".format(elevacion))
elif opcion == "2":
    numero1 = input("ingrese numero que quiere elevarlo")
    numero2 = input("ingrese segundo numero")
    numero3 = input("ingresar tercer numero")
    elevacion = int(numero1) ** int(numero2) ** int(numero3)
    print("la levacion es:. {}".format(elevacion))
else:
    print("¡¡¡¡¡¡¡¡¡opcion no valida!!!!!!!!!!")
    

    
