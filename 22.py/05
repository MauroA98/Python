while True:

    # --- PASO 1: Pedir un número entero ---
    entrada = input("\nIngresá un número entero (0 para salir): ")

    try:
        numero = int(entrada)
    except ValueError:
        print("Eso no es un número entero. Fin del programa.")
        break

    if numero == 0:
        print("Ingresaste 0. Fin del programa.")
        break

    print(f"Número ingresado: {numero}. ¡El programa continúa!")

    # --- PASO 2: Pedir una palabra o frase ---
    frase = input("Ingresá una palabra o frase: ")

    cantidad = len(frase)
    print(f"La frase tiene {cantidad} caracteres.")

    # --- PASO 3: Calcular el factorial con un bucle for ---
    factorial = 1
    for i in range(1, cantidad + 1):
        factorial = factorial * i

    print(f"El factorial de {cantidad} es: {factorial}")

    # --- PASO 4: Par o impar ---
    if factorial % 2 == 0:
        print("El resultado es PAR.")
    else:
        print("El resultado es IMPAR.")