#API.py

#Importacion de las librerias panda y sodapy para la correcta consulta de los registros
import pandas as pd
from sodapy import Socrata

def obtener_datos(departamento, limite_registros):
    #Se obtienen los datos de la API
    client = Socrata("www.datos.gov.co", None)
    #Obtenemos los diccionarios por medio de sodapy, se utiliza where para filtrar el departamento ingresado, se utiliza select para filtrar las columnas deseadas
    results = client.get("gt2j-8ykr", where="departamento_nom = '{}'".format(departamento.upper()), 
                     select="ciudad_municipio_nom, departamento_nom, edad, fuente_tipo_contagio, estado, pais_viajo_1_nom",
                     limit=limite_registros,)

    results_df = pd.DataFrame.from_records(results)
    #Comprobamos que la columna "Pais de Origen" existe en nuestro DataFrame
    comprobar_columna = 'pais_viajo_1_nom' in results_df.columns

    if comprobar_columna == False:
        results_df[''] = "" #Arreglo para lograr conseguir la visualizacion de la columna "Pais de Origen"

    #Renombro las columnas para facil comprension por parte del usuario
    results_df.columns = ['Ciudad de Ubicacion', 'Departamento', 'Edad', 'Tipo', 'Estado', 'Pais de Origen']
    
    return results_df
