productos = [('laptop', 1200, 5), ('mouse', 25, 50), ('teclado', 100, 30)]
def productoMasCaro(productos):
    productoCaro = productos[0]

    for producto in productos:
        if producto[1] > productoCaro[1]:
            productoCaro = producto
    return productoCaro

resultado = productoMasCaro(productos)
print(resultado)