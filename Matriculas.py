#Creo las listas de las personas que matricularon Programación III y Programación IV
matricula_prog_III = {
    'Luis': True,
    'Juanita': False,
    'Jeronimo': True,
    'Diego': True,
    'Angie': False
}

matricula_prog_IV = {
    'Luis': True,
    'Juanita': True,
    'Jeronimo': True,
    'Diego': False,
    'Angie': False
}

# Obtengo la lista de las personas que tienen matriculadas ambas materias verificando si estan en ambas listas
alumnos_ambas_materias = []
for alumno in matricula_prog_III:
    if alumno in matricula_prog_IV and matricula_prog_III[alumno] and matricula_prog_IV[alumno]:
        alumnos_ambas_materias.append(alumno)

# Imprimo la lista de alumnos que tienen matriculadas ambas materias
print("Alumnos matriculados en Programación III y Programación IV a la vez:")
print(alumnos_ambas_materias)