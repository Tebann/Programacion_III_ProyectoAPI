#API.py

import pandas as pd
from sodapy import Socrata

def obtener_datos(departamento, limite_registros):
#Se obtienen los datos de la API
    client = Socrata("www.datos.gov.co", None)

    results = client.get("gt2j-8ykr", where="departamento_nom = '{}'".format(departamento.upper()), 
                        select="ciudad_municipio_nom, departamento_nom, edad, fuente_tipo_contagio, estado",
                        limit=limite_registros,)
    
    results_df = pd.DataFrame.from_records(results)
    results_df.columns = ['Ciudad de Ubicacion', 'Departamento', 'Edad', 'Tipo', 'Estado']
    
    return results_df