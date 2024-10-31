
print("")
print("guzman 1188")
print("")
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "ecosistemas"]#se enseñan las materias en pantalla
asignaturas_repetir = []# Iniciar una lista para las asignaturas que hay que repetir
for asignatura in asignaturas:# Preguntar al usuario la nota de cada asignatura
    try:
        nota = float(input(f"¿Qué nota sacaste en {asignatura}? "))#se le preguntara que nota saco en cada matera
        if nota < 6:  # Supongamos que la nota mínima para aprobar es 6
            asignaturas_repetir.append(asignatura)#si tine menos de 6 la materia se agregara a otrea lista
    except ValueError:
        print("Por favor, introduce un número válido.")
if asignaturas_repetir:# Mostrar las asignaturas que hay que repetir
    print("Tienes que repetir las siguientes asignaturas:")#se imprimira el mensaje que ay que repetir
    for asignatura in asignaturas_repetir:
        print(f"- {asignatura}")#se imprimen las materias reprobadas
else:
    print("¡Felicidades! Has aprobado todas las asignaturas.")
    