def contiene_sublista(lista, sublista):
    for elemento in lista:
        if isinstance(elemento, list):
            if elemento == sublista:
                return True
            elif contiene_sublista(elemento, sublista):
                return True
    return False

lista = [3.14, "Hola Doc!", [911, "Los chicos malos"]]
sublista = [911, "Los chicos malos"]
if contiene_sublista(lista, sublista):
    print("La lista contiene la sublista.")
else:
    print("La lista no contiene la sublista.")


for elemento in lista:
    if type(elemento) == list:
        print("La lista contiene la sublista.")
    else:
        print("La lista no contiene la sublista.")