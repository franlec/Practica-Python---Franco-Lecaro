temperaturas = [22.5, 23.0, 21.0, 19.5, 25.0, 26.5, 24.0]

def informeTemperatura(temperaturas):

    temperaturaMax = max(temperaturas)
    temperaturaMin = min(temperaturas)
    promedio = (sum(temperaturas) / len(temperaturas))
    return f"El promedio de temperatura es: {promedio}\n La temperatura maxima fue: {temperaturaMax}\n La temperatura minima fue: {temperaturaMin}"

print(informeTemperatura(temperaturas))
