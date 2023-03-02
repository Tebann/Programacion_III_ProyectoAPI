def cantidad_pasajeros():
    pasajeros = []
    pasajero = int(input("Ingrese la edad del pasajero: "))
    pasajeros.append(pasajero)
    if pasajeros[0] == 0:
        print ("Error, la edad ingresas no es valida.")
    else:
        while pasajeros[-1] != 0:
            pasajero = str(input("Desea ingresar otra persona? [S/N]: "))
            if pasajero == "S" or pasajero == "s":
                pasajero =int(input("Ingrese la edad del pasajero: "))
                pasajeros.append(pasajero)
            else:
                print()
                break

    print ("Total de pasajeros: ",len(pasajeros))

    longitud = len(pasajeros)
    i = 0
    costo = 0.00
    while i != longitud:
        if pasajeros[i] <= 3:
            costo = costo + 0.0
            i+=1
        elif pasajeros [i] > 3 and pasajeros [i] <= 11:
            costo = costo + 16.00
            i+=1
        elif pasajeros [i] > 11 and pasajeros [i] <= 50 :
            costo = costo + 34.00
            i+=1
        elif pasajeros [i] > 50:
            costo = costo + 40.00
            i+=1
        else:
            print ()

    print("El costo total es:",round(costo, 2)) #Utilizo el round para mostrar dos decimales
        
cantidad_pasajeros()