def cifrarYDescifrar(cadena, clave):
    resultado = ""
    for letra in range(len(cadena)):
        letraCadena_ascii = ord(cadena[letra])
        letraClave_ascii = ord(clave[letra % len(clave)])
        resultado += chr(letraCadena_ascii ^ letraClave_ascii)
    print(resultado)

    # 1. Coger letra cadena y pasar a ascii
    # 2. Coger letra clave y pasar a ascii
    # 3. XOR de asciiS
    # 4. Meter letra correspondiente al ascii en cadena de texto (resultado)


if __name__ == '__main__':
    print("1.Cifrar")
    print("2.Descifrar")
    op = int(input())
    if op==1:
        print("Cadena a cifrar:", end="")
        cadena = str(input())
        print("Clave:", end="")
        clave = str(input())
        cifrarYDescifrar(cadena, clave)
    elif op==2:
        print("Cadena a descifrar:", end="")
        cadena = str(input())
        print("Clave:", end="")
        clave = str(input())
        cifrarYDescifrar(cadena, clave)



