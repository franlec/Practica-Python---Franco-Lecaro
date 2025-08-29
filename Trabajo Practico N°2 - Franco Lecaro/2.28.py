biblioteca = {
    "El señor de los anillos": {"autor": "J.R.R. Tolkien", "año": 1954, "género": "Fantasía"},
    "Cien años de soledad": {"autor": "Gabriel García Márquez", "año": 1967, "género": "Realismo mágico"},
    "El código Da Vinci": {"autor": "Dan Brown", "año": 2003, "género": "Suspenso"}
}

def listarLibros(diccionario):
    librosPost2000 = []
    for titulo, info in diccionario.items():
        if info['año'] > 2000:
            librosPost2000.append(titulo)
    return librosPost2000

print(listarLibros(biblioteca))



