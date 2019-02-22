PRH = 1.5
hr = float(input("Cuantas horas deseeas estar?"))
if hr > 0 and hr < 5:
    total = hr * PRH
    print("El total a pagar es {}".format(total))
elif hr >=5:
    print("TIENES UNA HORA GRATIS")
    total2 = hr * PRH
    print("el total a pagar es de {}".format(total2))
