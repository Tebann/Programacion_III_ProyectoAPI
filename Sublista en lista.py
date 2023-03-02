lista = [4.555, "Bienvenidos a la UTP!", [222, "Programacion III"]]
i = -1
for elemento in lista:
    i+=1
    if type(elemento) == list:
        print("Lista Detectada!: ",elemento, "en el elemento ", i)
    else:
        print ("Lista no detectada en el elemento", i)