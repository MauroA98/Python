"""
def calcular_promedio(notas):
    
    total = sum(notas)
    cantidad = len(notas)
    return total / cantidad

# Ejemplo de uso:
mis_notas = [8, 7, 9, 6, 10]
resultado = calcular_promedio(mis_notas)
print(f"El promedio es: {resultado}")
"""

def calcular_promedio_interactivo():
    suma_total = 0
    cantidad = 0
    
    print("Ingresa tus notas (escribe 'fin' para terminar):")
    
    while True:
        entrada = input(f"Nota {cantidad + 1}: ")
        
        if entrada.lower() == 'fin':
            break
            
        try:
            nota = float(entrada)
            # Validamos que sea una nota lógica (ej: entre 0 y 10)
            if 0 <= nota <= 10:
                suma_total += nota
                cantidad += 1
            else:
                print("Por favor, ingresa una nota entre 0 y 10.")
        except ValueError:
            print("Entrada inválida. Ingresa un número o 'fin'.")
    
    if cantidad > 0:
        promedio = suma_total / cantidad
        print(f"\nSe ingresaron {cantidad} notas.")
        print(f"El promedio es: {promedio:.2f}")
    else:
        print("No se ingresaron notas para calcular.")


calcular_promedio_interactivo()