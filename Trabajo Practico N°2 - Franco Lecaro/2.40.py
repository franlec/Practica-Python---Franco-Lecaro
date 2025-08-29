estudiantes = {
    101: {"matemáticas": [85, 90, 78], "ciencias": [88, 85, 80]},
    102: {"matemáticas": [92, 88, 84], "ciencias": [75, 80, 85]},
    103: {"matemáticas": [78, 85, 88], "ciencias": [90, 95, 92]}
}

def rankingPromedio (estudiantes):
    ranking = []
    notasMate = 0
    for clave in estudiantes:
        promedio = (sum(estudiantes[clave]["matemáticas"])+sum(estudiantes[clave]["ciencias"])) / (len(estudiantes[clave]["matemáticas"])+len(estudiantes[clave]["ciencias"]))
        ranking.append((clave,promedio))
    ranking.sort(key=lambda x: x[1], reverse=True)
    return ranking

print(rankingPromedio(estudiantes))
