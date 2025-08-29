notas_estudiantes = [
    ("Ana", [85, 90, 78]),
    ("Luis", [88, 92, 80]),
    ("María", [75, 85, 70])
]

def promedioCalificaciones (lista):
    promedioCalif = {}

    for nombre, notas in lista:
        promedio = sum(notas) / len(notas)
        promedioCalif[nombre] = promedio
    return promedioCalif

print(promedioCalificaciones(notas_estudiantes))


