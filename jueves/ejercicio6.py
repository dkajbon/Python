NUEVO_SALARIO = 0.8
DESCUENTO = 0.025
salario = int(input("ingrese salario atual:"))
incremento = salario * NUEVO_SALARIO
suma = salario + incremento
descuento = suma * 0.025
resta = suma - descuento
print("su sueldo nuevo es de :{}".format(resta))
