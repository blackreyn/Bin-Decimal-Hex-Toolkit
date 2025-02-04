def decimal_to_binary(decimal):
    
    decimal_inicial = decimal
    binary = ""

    if decimal == 0:
        binary += "0"

    while decimal > 0:

        if decimal == 1:
            # Aquí tenemos el último cociente que siempre es = 1
            binary += "1"
            break

        elif decimal % 2 == 1:
            binary += "1"
        
        else:
            binary += "0"

        decimal = int(decimal / 2)

    # Los nº binarios se calculan cogiendo los residuos de forma inversa que resultan de dividir el nº entre 2  
    binary = binary[::-1]
    print("El número", decimal_inicial, "en binario es", binary)


decimal_to_binary(1)
decimal_to_binary(10)
decimal_to_binary(64)

