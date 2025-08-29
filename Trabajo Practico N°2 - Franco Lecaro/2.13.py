estudiantes = {
    101: {"nombre": "Ana", "edad": 16, "calificaciones": {"matemáticas": 85, "ciencias": 90}},
    102: {"nombre": "Luis", "edad": 17, "calificaciones": {"matemáticas": 78, "ciencias": 88}}
}

def promCalificaciones(matricula):
    calificaciones = estudiantes[matricula]["calificaciones"]
    promedio = sum(calificaciones.values()) / len(calificaciones)
    return promedio

print("El promedio de Ana es: ",promCalificaciones(101))
print("El promedio de Luis es: ",promCalificaciones(102))
