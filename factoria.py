def factorial(n):
    # El factorial de 0 y 1 siempre es 1 (caso base)
    if n == 0 or n == 1:
        return 1
    resultado = 1
    # El bucle se repetirá desde 2 hasta n para calcular el factorial
    for i in range(2, n + 1):
        # Multiplicamos el resultado acumulado por cada número desde 2 hasta n
        resultado *= i
    return resultado

# Solicitamos al usuario un número para calcular su factorial
numero = int(input("Ingresá un número entero positivo: "))
print(f"El factorial de {numero} es: {factorial(numero)}")