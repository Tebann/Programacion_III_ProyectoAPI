#main.py

import API
import UI

def main():
#Funcion principal que ejecuta nuestro programa
    departamento = UI.obtener_departamento()
    limite_registros = int(UI.obtener_limite_registros())
    resultados = API.obtener_datos(departamento, limite_registros)
    UI.mostrar_resultados(resultados)

if __name__ == '__main__':
    main()

input("Presione cualquier tecla para salir...")
