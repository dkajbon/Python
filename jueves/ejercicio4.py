Euros_Dolar = 2150
Dolar_Euros = 145
cantidad = 0
total = 0
print("Bienvenido al conversor".center(50,"*"))
opcion=input(" 1- euros a dolares 2- dolares a euros:.")

if opcion == "1":
    Euros = input("cantidad de Euros")
    saldo = float(Euros) / Euros_Dolar
    print("La convercion es {}".format(saldo))
elif opcion == "2":
    dolares = input ("canidad de dolares")
    saldo = float (dolares) * Dolar_Euros
    print("La convercion es {}".format(saldo))
else:
    print("Opcion no valida")
                        
