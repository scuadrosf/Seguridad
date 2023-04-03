import base64


def decodificar(cifrado):
    decodificado = base64.b64decode(cifrado).decode("utf-8")
    print(decodificado)


if __name__ == '__main__':
    cifrado = str(input())
    decodificar(cifrado)