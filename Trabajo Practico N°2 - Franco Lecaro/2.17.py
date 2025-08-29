empleados = {
    1: ("Ana", 30, 3000),
    2: ("Luis", 25, 2500),
    3: ("María", 35, 4000)
}

def gananMas (diccionario, salario):
    resultado = {}
    for id, datos in diccionario.items():
        if datos[2] >= salario:
            resultado[id] = datos
    return resultado

print(gananMas(empleados, 3500))

