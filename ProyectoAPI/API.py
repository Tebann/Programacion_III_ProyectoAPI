#API.py

import pandas as pd
from sodapy import Socrata

def obtener_datos(departamento, limite_registros):
#Se obtienen los datos de la API
    client = Socrata("www.datos.gov.co", None)

    results = client.get("gt2j-8ykr", where="departamento_nom = '{}'".format(departamento.upper()), 
                     select="ciudad_municipio_nom, departamento_nom, edad, fuente_tipo_contagio, estado, pais_viajo_1_nom",
                     limit=limite_registros,)

    results_df = pd.DataFrame.from_records(results)
    prueba = 'pais_viajo_1_nom' in results_df.columns

    if prueba == True :
        results_df.columns = ['Ciudad de Ubicacion', 'Departamento', 'Edad', 'Tipo', 'Estado', 'Pais de Origen']
    else:
        results_df.columns = ['Ciudad de Ubicacion', 'Departamento', 'Edad', 'Tipo', 'Estado']

    results_df['Pais de Origen']=""
    
    return results_df