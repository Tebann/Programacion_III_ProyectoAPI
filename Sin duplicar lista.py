lista = ['ref-010', 'ac-090', 'ref-010', 'xp-89', 'as-65', 'kj-11', 'xp-89', 'wx-23', 'rk-87', 'as-65']

lista_sin_error = []
for codigo in lista:
    if codigo not in lista_sin_error: #Si un codigo ya se encuentra regsitrado en la lista sin errores, este no volverá a ser reescrito
        lista_sin_error.append(codigo)

print(lista_sin_error)