print("")
print("guzman jared 1188")
print("")
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "ingles"]
notas = {}#diccionario

for asignatura in asignaturas:
    try:
        nota = float(input(f"¿Qué nota sacaste en {asignatura}? "))
        notas[asignatura] = nota
    except ValueError:
        print("Por favor, introduce un número válido.")
for asignatura, nota in notas.items():
    print(f"En {asignatura} has sacado {nota}")#se muestra la asignatura con su calificacion

