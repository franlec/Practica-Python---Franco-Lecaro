
def configurar_perfiles(usuarios, **kwargs):
    perfiles = {}
    for usuario in usuarios:
        perfiles[usuario] = list(kwargs.values())
    return perfiles

usuarios = ["Ana", "Luis", "María"]

resultado = configurar_perfiles(usuarios, idioma="es", modo_oscuro=True, notificaciones=False)
print(resultado)
