nombre=input("dime tu nombre")
print("hola {}, hoy vamos a jugar a un juego".format(nombre))
respuesta=int(input("¿estas listo?"))
if respuesta == 1:
    print("ok {}, pues empecemos".format(nombre))
    number_to_gess = 5
    user_number = int(input("dime un numero del uno al 10"))
    if user_number == number_to_gess:
        print("ganaste")
    else:
        print("perdiste, intentalo de nuevo")
    user_number = int(input("dime un numero del uno al 10"))
    if user_number == number_to_gess:
        print("ganaste")
    else:
        print("perdiste, intentalo de nuevo")
    user_number = int(input("dime un numero del uno al 10"))
    if user_number == number_to_gess:
        print("ganaste")
    else:
        print("perdiste, intentalo de nuevo")
    user_number = int(input("dime un numero del uno al 10"))
    if user_number == number_to_gess:
        print("ganaste")
    else:
        print("perdiste, intentalo de nuevo")
    user_number = int(input("dime un numero del uno al 10"))
    if user_number == number_to_gess:
        print("ganaste")
    else:
        print("perdiste, gracias por participar")

else:
    print("pues vete a la chingada")
print("adios")