"# Escribe una función que reciba un color y determine si es un color primario o no."
"""
def es_primario(color):
    
    colores_primarios = ["rojo", "azul", "amarillo"]
    
    if color.lower() in colores_primarios:
        print(f"El color {color} es primario")
    else:
        print(f"El color {color} no es primario, pendejo")

es_primario("rojo")    # → El color rojo es primario
es_primario("verde")   # → El color verde no es primario
"""
def es_primario(color):
    colores_primarios = ["rojo", "azul", "amarillo"]
    
    if color.lower() in colores_primarios:
        print(f"El color {color} es primario.")
    else:
        print(f"El color {color} no es primario.")


color_usuario = input("Ingresa un color para verificar si es primario: ")

# Llamamos a la función con el dato ingresado
es_primario(color_usuario)