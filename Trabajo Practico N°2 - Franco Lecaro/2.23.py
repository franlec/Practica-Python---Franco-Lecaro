inventario = [50, 30, 20, 10]
ventas = [5, 10, 5, 2]

def actualizarInventario (inventario, ventas) :
    inventarioActualizado =[]

    for x in range(len(inventario)):
        inventarioActualizado.append((inventario[x] - ventas[x]))
    return inventarioActualizado

print(actualizarInventario(inventario, ventas))