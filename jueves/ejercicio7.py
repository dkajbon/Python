URGENCIA = 0.37
PEDIATRIA = 0.42
TRAUMATOLOGIA = 0.21
print("Desea calcular presupuesto")
salida = input("ingresar presupuesto 1-si 2-no")
while salida != 2:
    presupuesto = int(input("ingresar cantidades"))
    print("La cantidad es:.{}".format(presupuesto * URGENCIA))
    print("La cantidad es:.{}".format(presupuesto * PEDIATRIA))
    print("La cantidad es:.{}".format(presupuesto * TRAUMATOLOGIA))
    salida = input("Ingresar presupuesto 1-si  2-no")
print ("Gracias")
    
