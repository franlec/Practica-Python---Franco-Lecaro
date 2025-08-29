

def publicar (nombre,titulo,**kwargs):
    infoPublicacion = {
        "nombre": nombre,
        "titulo": titulo,
    }
    infoPublicacion.update(kwargs)
    return infoPublicacion

print(publicar("Juan", "Mi primer post!", etiquetas=["#hola", "#primerPost"], visibilidad="publica", likes=100))

