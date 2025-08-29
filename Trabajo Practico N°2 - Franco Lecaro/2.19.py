resultados = {
    "Equipo A": (3, 2),
    "Equipo B": (1, 1),
    "Equipo C": (4, 0)
}

def informeGoles (diccionario):
    golesAFavor = 0
    golesEnContra = 0
    for x in diccionario.values():
        golesAFavor += x[0]
        golesEnContra += x[1]
    return f"Los goles a favor de los equipos son: {golesAFavor} y los goles en contra son: {golesEnContra}"

print(informeGoles(resultados))
