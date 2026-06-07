"# Escribe una función que reciba una lista de números y devuelva el número mayor."
"""
def numero_mayor(numeros):
    # max() devuelve el valor más alto de la lista
    mayor = max(numeros)
    print(f"El número mayor es: {mayor}")
    return mayor

# Ejemplo de uso:
serie = [4, 12, 7, 3, 55, 5]
numero_mayor(serie)   # → El número mayor es: 55

"""
def encontrar_numero_mayor():
    mayor = None
    cantidad = 0
    
    print("Ingresa números para encontrar el mayor (escribe 'fin' para terminar):")
    
    while True:
        entrada = input(f"Introduce el número {cantidad + 1}: ")
        
        if entrada.lower() == 'fin':
            break
            
        try:
            numero = float(entrada)
            
            # Si es el primer número o es mayor al guardado, lo actualizamos
            if mayor is None or numero > mayor:
                mayor = numero
            
            cantidad += 1
            
        except ValueError:
            print("Entrada inválida. Ingresa un número o 'fin'.")
    
    if mayor is not None:
        print(f"\nEl número mayor ingresado es: {mayor}")
    else:
        print("No se ingresaron números.")

# Llamamos a la función
encontrar_numero_mayor()