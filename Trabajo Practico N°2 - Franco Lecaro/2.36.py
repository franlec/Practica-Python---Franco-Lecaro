inventario = {

    "Tienda A": {"producto_1": 50, "producto_2": 30},
    "Tienda B": {"producto_1": 20, "producto_2": 40}
}

def actualizar_inventario (diccionario, **kwargs):

    tienda = kwargs.pop("tienda")

    for producto, cantidad in kwargs.items():
        diccionario[tienda][producto] = cantidad
    return diccionario

print(actualizar_inventario(inventario,tienda="Tienda A", producto_1=10, producto_2=-5))








