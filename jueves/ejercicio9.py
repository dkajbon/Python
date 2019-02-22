valor_h = 0
h = 0
ho_ex = 0
valor_horas = int(input("Valor de las horas"))
hora = int(input("Horas que trabaja"))
hora_extra = int(input("Horas extras echas"))
valor_h = int(valor_horas)*int(hora) 
h = int(valor_horas) * int(hora_extra)*int(2)
ho_ex = int(valor_horas)+int(valor_horas)*int(hora_extra)*int(2)
print("Su sueldo normal es:.{}".format(valor_h))
print("Su sueldo extra es:.{}".format(h))
print("El total es:.{}".format(ho_ex))
