

def simular_ventas (*args):
    totalIngresos = 0
    for arg in args:
        nombre = arg[0]
        cantidad = arg[1]
        precio = arg[2]
        ingresos = cantidad * precio
        print(f"Nombre: {nombre} ingresos generados: {ingresos}")
        totalIngresos += ingresos
    return print(f"El total de ingresos generados es: {totalIngresos}")

simular_ventas(("Producto A", 10, 15.0), ("Producto B", 5, 25.0), ("Producto C", 3, 50.0))

