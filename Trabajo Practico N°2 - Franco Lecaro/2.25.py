
def analizar_finanzas(**kwargs):
    balance = sum(kwargs.values())
    print(f"El balance total es:",balance)

analizar_finanzas(sueldo=2000, renta=-800, transporte=-150, comida=-300, freelance=500)

