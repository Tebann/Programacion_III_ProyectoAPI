#main.py

#importacion de los modulos correspondientes para el correcto funcionamiento
import API
import UI

def main():
#Funcion principal que ejecuta nuestro programa
    departamento = UI.obtener_departamento()
    limite_registros = int(UI.obtener_limite_registros())
    resultados = API.obtener_datos(departamento, limite_registros)
    UI.mostrar_resultados(resultados)

#Verificacion main, para ejecutar como el programa principal
if __name__ == '__main__':
    main()

input("Presione cualquier tecla para salir...") 
