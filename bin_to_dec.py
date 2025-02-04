"""
 Reto #38
 BINARIO A DECIMAL
 Dificultad: MEDIA
  Enunciado: Crea un programa se encargue de transformar un número binario
  a decimal sin utilizar funciones propias del lenguaje que
  lo hagan directamente.
"""
import math

def binary_to_decimal(number):
    binary_inicial = str(number)[::-1]
    bin = str(binary_inicial)[::-1]
    decimal = 0

    # El primer elemento (último) es elevado a 1
    for i in range(0, len(binary_inicial)):
        binary_str = str(binary_inicial)

        if binary_str[i] == "1":
            # Con el for conseguimos obtener el índice i necesario para elevar 2 y sumarlo
            decimal += 2 ** i
            #decimal += math.pow(2, i)
    
    return print(f"\n[+]El número binario {bin} en decimal es {decimal}")

#binary_to_decimal(1)

# Es 1
#binary_to_decimal(1)

#4
#binary_to_decimal(100)

#43
#binary_to_decimal(101011)

#100
#binary_to_decimal(1100100)

#725
#binary_to_decimal(1011010101)

#387
binary_to_decimal(110000011)
