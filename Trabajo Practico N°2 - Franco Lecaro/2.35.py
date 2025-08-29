rutas = [("Madrid", "Barcelona", 620),
         ("Madrid", "Valencia", 350),
         ("Barcelona", "Valencia", 350)]
distancias_max = [600, 400, 500]

def rutasPermitidas (rutas, distancias_max):

    for i, ruta in enumerate(rutas):
        if ruta[2] > distancias_max[i]:
            return f"La ruta {ruta[0]}-{ruta[1]} no cumple con la distancia {distancias_max[i]}"
    return "Todas las rutas cumplen con la distancia maxima"

print(rutasPermitidas(rutas, distancias_max))


