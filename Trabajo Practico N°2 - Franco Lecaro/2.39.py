precios_diarios = [100, 105, 102, 110, 108]
operaciones = [("compra", 0), ("venta", 3), ("compra", 2), ("venta", 4)]


def calcular(precios_diarios, operaciones):
    beneficioTotal = 0
    for tipo,dia in operaciones:

        if tipo == "compra":
            precioDeCompra = precios_diarios[dia]

        elif tipo == "venta":
            precioDeVenta = precios_diarios[dia]
            beneficioTotal += precioDeVenta - precioDeCompra


    return f"El beneficio total es de: {beneficioTotal}"

print(calcular(precios_diarios, operaciones))
