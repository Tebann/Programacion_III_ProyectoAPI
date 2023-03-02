def promedio_estaturas():
    estaturas = []
    estatura = int(input("Ingrese la estatura: "))
    estaturas.append(estatura) #Utilizo .append para agregar cada estatura al final de la lista.
    if estaturas[0] == 0:
        print ("Error, la estatura ingresas no es valida.") #Si la primera estatura es 0, muestra un error apropiado
    else:
        while estaturas[-1] != 0:
            estatura = str(input("Desea ingresar mas estaturas [S/N]: "))
            if estatura == "S" or estatura == "s":
                estatura =int(input("Ingrese la estatura: "))
                estaturas.append(estatura)
            else:
                print()
                estaturas.append(estatura)
                break
                
    estaturas.pop() #Utilizo el .pop para eliminar el ultimo elemento de la lista, para realizan la division correctamente
    promedio = 0

    for i in estaturas:
        promedio = promedio + i

    total_datos = len(estaturas) #Utilizo el .len para saber la longitud de la lista
    promedio = promedio/total_datos
    print ("El promedio de estaturas es :",(promedio))

promedio_estaturas()


