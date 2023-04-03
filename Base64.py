import base64


def codificar(en_claro):
    binario = en_claro.encode("utf-8")
    codificado = base64.b64encode(binario).decode("utf-8")
    print("Codificado:", codificado)


def decodificar(cifrado):
    decodificado = base64.b64decode(cifrado).decode("utf-8")
    print("Decodificado:", decodificado)
    return decodificado


if __name__ == '__main__':
    cifrado = str(input())
    decodificado = decodificar(cifrado)
    codificar(decodificado)
