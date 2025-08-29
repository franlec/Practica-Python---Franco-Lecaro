puntuaciones = [("Ana", 85), ("Luis", 90), ("María", 78)]

def puntuacionesOrdenadas(lista):
    return sorted(lista, key= lambda x: x[1], reverse=True)

print(puntuacionesOrdenadas(puntuaciones))