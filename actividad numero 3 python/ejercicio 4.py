valor = int(input("cuantas notas quiere ingresar "))
suma = 0
for i in range(valor):
    nota= int(input("ingrese nota:"))
    suma = suma  + int(nota)
    promedio = suma / nota
print("el promedio es:.{}".format(promedio))
