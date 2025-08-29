ventas_mensuales = [2000, 2500, 3000, 2800, 3500, 4000, 4200, 3800, 3600, 3900, 4100, 4500]

def estadisticasVentas (array):
    diccionarioVentas = {}
    totalVentas = sum(array)
    promedioVentas = totalVentas / len(array)
    maxVentas = max(array)

    diccionarioVentas['Total de ventas'] = totalVentas
    diccionarioVentas['Promedio de ventas'] = promedioVentas
    diccionarioVentas['Maximo de ventas en un dia'] = maxVentas

    return diccionarioVentas

print(estadisticasVentas(ventas_mensuales))

