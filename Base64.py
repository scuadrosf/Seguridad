import base64


def codificar(en_claro):
    binario = en_claro.encode("utf-8")
    codificado = base64.b64encode(binario).decode("utf-8")
    print("Cifrado:", codificado)


def decodificar(cifrado):
    decodificado = base64.b64decode(cifrado).decode("utf-8")
    print("Descifrado:", decodificado)
    return decodificado


if __name__ == '__main__':
    print("1.Cifrar")
    print("2.Descifrar")
    print("3.Los 2")
    op = int(input())
    if op==1:
        enClaro = str(input())
        codificar(enClaro)
    elif op==2:
        codificado = str(input())
        decodificar(codificado)
    else:
        codificado = str(input())
        enClaro = decodificar(codificado)
        codificar(enClaro)

