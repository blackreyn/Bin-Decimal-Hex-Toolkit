# Conversión de Hexadecimal a Decimal
def hexadecimal_a_decimal(hexadecimal):
    # Convertir de hexadecimal a decimal
    return int(hexadecimal, 16)

# Definir el número hexadecimal directamente en el código
numero_hexadecimal = "0xFF"  # Cambia este valor según sea necesario

# Conversión de hexadecimal a decimal
resultado = hexadecimal_a_decimal(numero_hexadecimal)
print(f"El número hexadecimal {numero_hexadecimal} en decimal es: {resultado}")
