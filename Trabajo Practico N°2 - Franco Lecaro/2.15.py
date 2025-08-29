calcular_promedio= (85, 90, 78, 92)

def promedio(*args):
    promedio = sum(args) / len(args)
    return promedio
print(promedio(85, 90, 78, 92))
