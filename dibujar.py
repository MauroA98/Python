def dibujar_rectangulo(filas, columnas):
    # range(n) genera los números de 0 hasta n-1
    # El bucle for repite el bloque interno "n" veces
    for i in range(filas):
        # El operador * repite el string N veces
        print("* " * columnas)

# Ejemplo de uso:
filas = int(input("Ingresá la cantidad de filas: "))
columnas = int(input("Ingresá la cantidad de columnas: "))
dibujar_rectangulo(filas, columnas)