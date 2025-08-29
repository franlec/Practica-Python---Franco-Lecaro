
def registro_empleado (nombre, edad, salario,**kwargs):
    diccionarioEmpleado = {
        "nombre": nombre,
        "edad": edad,
        "salario": salario,
    }
    diccionarioEmpleado.update(kwargs)
    return diccionarioEmpleado

print(registro_empleado("Ana", 30, 3000, direccion="Calle Falsa 123", telefono="123456789"))