ventas_diarias = [200, 450, 300, 400, 350, 500, 600]

def informeVentas(array):
    total = sum(array)
    promedio = sum(array) / len(array)
    return f"El promedio de ventas diarias es: {promedio}, y el total de ventas es: {total} "
print(informeVentas(ventas_diarias))