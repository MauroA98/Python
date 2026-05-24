#1

"""
numero = int(input("Ingresa un número: "))

if numero % 2 == 0:
    print("El número es PAR")
else:
    print("El número es IMPAR")
"""

#2

""""
numero = int(input("Ingresa un número: "))

for i in range(1, 11):
    print(numero, "x", i, "=", numero * i)
"""

#3

"""
nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print(nombre, "es mayor de edad")
else:
    print(nombre, "es menor de edad")
"""

#4

"""
palabra = input("Ingresa una palabra: ")
veces = int(input("¿Cuántas veces? "))

for i in range(veces):
    print(palabra)
"""

#5

"""
suma = 0

while True:
    numero = int(input("Ingresa un número (0 para terminar): "))
    if numero == 0:
        break
    suma = suma + numero

print("La suma total es:", suma)

"""

#6

"""
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")

nombre = nombre.capitalize()
apellido = apellido.capitalize()

print("Tu nombre es:", nombre, apellido)
"""

#7

"""edad = int(input("Ingresa tu edad: "))

if edad < 16:
    print("No estás habilitado para votar")
elif edad >= 18:
    print("Estás obligado a votar")
else:
    # Tiene entre 16 y 17 años
    decision = input("Tenés entre 16 y 17 años. ¿Decidís votar? (si/no): ")
    if decision.lower() == "si":
        print("¡Genial! Vas a votar")
    else:
        print("De acuerdo, no votás")
"""

#8

"""suma = 0

while True:
    numero = float(input("Ingresa un número (0 para terminar): "))
    if numero == 0:
        break
    suma = suma + numero ** 2

print("La suma de los cuadrados es:", suma)"""