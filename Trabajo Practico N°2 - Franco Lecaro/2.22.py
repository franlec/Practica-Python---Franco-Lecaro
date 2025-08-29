paquetes = [
    ("Paris", 200, 5),
    ("Roma", 150, 4),
    ("Londres", 180, 3)
]

def diccionarioPaquetes(array):
    diccionario = {}

    for destino, precio, dias in array:
        total = dias * precio
        diccionario[destino] = total
    return diccionario

print(diccionarioPaquetes(paquetes))

