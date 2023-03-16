#main.py

#Importacion de los modulos correspondientes para el correcto funcionamiento
import API
import UI

#Funcion principal que ejecuta nuestro programa
def main():
    departamento = UI.obtener_departamento()                #Llamado a la funcion para obtener el departamento
    UI.comprobar_departamento(departamento.upper())         # Llamado a la funcion para la comprobacion de la existencia del departamento
    limite_registros = int(UI.obtener_limite_registros())   #Lamado a la funcion para obtener el numero de registro
    UI.comprobar_limite(limite_registros)                   # Llamado a la funcion para comprobar que el limite sea menor a 1000 
    resultados = API.obtener_datos(departamento, limite_registros) #Llamado a la funcion para operar los datos ingresados por el usuario
    UI.mostrar_resultados(resultados)                       #Llamado a la funcion para mostrar el resultado al usuario

#Verificacion main, para ejecutar como el programa principal
if __name__ == '__main__':
    main()

input("Presione cualquier tecla para salir...")  
