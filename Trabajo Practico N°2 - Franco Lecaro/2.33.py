reservas = {
    "2024-08-15": [("Juan", 101, 150), ("Ana", 102, 180)],
    "2024-08-16": [("Luis", 101, 150)]
}

def realizarReserva (reservas, fecha,nombre, habitacion,precio):
    if fecha not in reservas:
        reservas[fecha] = []

    ocupada = False
    for x in reservas[fecha]:
        if x[1] == habitacion:
            ocupada = True
            break
    if ocupada:
        return f"La habitacion {habitacion} esta ocupada el {fecha}"
    else:
        reservas[fecha].append((nombre, habitacion, precio))
        return reservas

print(realizarReserva(reservas,"2025-08-15", "María", 103, 200))
print(realizarReserva(reservas,"2024-08-15", "María", 102, 180))




