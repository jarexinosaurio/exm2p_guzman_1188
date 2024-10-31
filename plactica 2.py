print("")
print("guzman 11888")
print("")
creditos = {'Matemáticas': 6, 'ecosistemas': 4, 'Química': 5}#las materias con sus creditos
for asignatura, credito in creditos.items():# Muestran los créditos de cada asignatura
    print(f"{asignatura} tiene {credito} créditos")#imprime la materia con sus creditos 
# Calcular y mostrar el total de créditos
total_creditos = sum(creditos.values())#se ara una suma para conoserel total
print(f"El número total de créditos del curso es: {total_creditos}")# se3 imprime el total de creditos
