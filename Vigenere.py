def cifrar(mensaje, clave, alfabeto):
    cifrado = ""
    n = len(alfabeto)
    for i in range(len(mensaje)):
        if mensaje[i] in alfabeto:
            x = alfabeto.index(mensaje[i])
            y = alfabeto.index(clave[i % len(clave)])
            if clave[i % len(clave)].isupper():
                cifrado += alfabeto[(x + y) % n].upper()
            else:
                cifrado += alfabeto[(x + y) % n]
        else:
            cifrado += mensaje[i]
    print("Mensaje cifrado:", cifrado)

def descifrar(cifrado, clave, alfabeto):
    mensaje = ""
    n = len(alfabeto)
    for i in range(len(cifrado)):
        if cifrado[i] in alfabeto:
            x = alfabeto.index(cifrado[i])
            y = alfabeto.index(clave[i % len(clave)])
            if clave[i % len(clave)].isupper():
                mensaje += alfabeto[(x - y) % n].upper()
            else:
                mensaje += alfabeto[(x - y) % n]
        else:
            mensaje += cifrado[i]
    print("Mensaje descrifrado:", mensaje)


if __name__ == '__main__':
    alfabeto = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    clave = "Vigenere"

    print("1.Cifrar")
    print("2.Descifrar")
    op = int(input())
    if op == 1:
        enClaro = str(input())
        cifrar(enClaro, clave, alfabeto)
    elif op == 2:
        codificado = str(input())
        descifrar(codificado, clave, alfabeto)