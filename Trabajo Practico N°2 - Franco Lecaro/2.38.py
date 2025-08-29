suscripciones = {
    "Jose": ["mensual", "anual"],
    "Ana": ["mensual"]
}

def actualizar_suscripcion (diccionario,usuario,suscripcion, **kwargs):

    if usuario not in diccionario:
        diccionario[usuario] = []

    diccionario[usuario].append(suscripcion)

    if kwargs:
        diccionario[usuario].append(kwargs)

    return diccionario

print(actualizar_suscripcion(suscripciones,usuario="Luis", suscripcion="mensual", auto_renovacion=True))

