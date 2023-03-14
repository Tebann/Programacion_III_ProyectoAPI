#UI.py

def obtener_departamento():
#Solicitamos el nombre del departamento al usuario
    return input("Ingrese el departamento deseado: ")

def obtener_limite_registros():
#Solicitamos el límite de registros al usuario
    print("RECOMENDACION: Ingrese un numero de registro pequeño")
    return input("Ingrese el numero de registro deseado: ")

def mostrar_resultados(resultados):
#Mostramos los resultados al usuario
    print(resultados)