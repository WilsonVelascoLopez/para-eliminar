# ejercicio No 1

estado = True
while (estado == True):
    numero = int(input("Digite un numero de 0 a 20 : "))

    if ((numero >= 0) and (numero <= 20)):
        print ("El numero ingresado es correcto")
        #estado = False
        break
    else:
        print ("Intentalo nuevamente")
