#UI.py

import API

#Solicitamos el nombre del departamento al usuario
def obtener_departamento():
    return input("Ingrese el departamento deseado: ")

#Solicitamos el límite de registros al usuario
def obtener_limite_registros():
    print("RECOMENDACION: Ingrese un numero menor a 1000")
    return input("Ingrese el numero de registro deseado: ")

#Comprobar que el numero de registro sea menor a 1000
def comprobar_limite(limite):
    if limite > 1000:
        input("Numero de registro no valido.")
        exit()
    else:
        return True

#Comprobacion de que el departamento ingresado sea correcto
lista_dep = API.crear_lista()
def comprobar_departamento(departamento):
    if (departamento not in lista_dep):
        print("Departamento no encontrado...")
        exit()
    else:
        return True

#Mostramos los resultados al usuario
def mostrar_resultados(resultados):
    print(resultados)
