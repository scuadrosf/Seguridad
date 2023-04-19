def vigenere_cifrado(mensaje, clave, alfabeto):
    cifrado = ""
    n = len(alfabeto)
    for i in range(len(mensaje)):
        if mensaje[i] in alfabeto:
            x = alfabeto.index(mensaje[i])
            y = alfabeto.index(clave[i % len(clave)].lower())
            if clave[i % len(clave)].isupper():
                cifrado += alfabeto[(x + y) % n].upper()
            else:
                cifrado += alfabeto[(x + y) % n]
        else:
            cifrado += mensaje[i]
    return cifrado

def vigenere_descifrado(cifrado, clave, alfabeto):
    mensaje = ""
    n = len(alfabeto)
    for i in range(len(cifrado)):
        if cifrado[i] in alfabeto:
            x = alfabeto.index(cifrado[i])
            y = alfabeto.index(clave[i % len(clave)].lower())
            if clave[i % len(clave)].isupper():
                mensaje += alfabeto[(x - y) % n].upper()
            else:
                mensaje += alfabeto[(x - y) % n]
        else:
            mensaje += cifrado[i]
    return mensaje

alfabeto = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
mensaje_cifrado = "QqmiaiiiYmisqmwmxijs"
clave = "Vigenere"

mensaje_descifrado = vigenere_descifrado(mensaje_cifrado, clave, alfabeto)
print("Mensaje descifrado:", mensaje_descifrado)
