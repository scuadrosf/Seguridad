import binascii

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import algorithms, Cipher, modes
from cryptography.hazmat.primitives.padding import PKCS7


def codificar(enClaroAux, clave, iv):
    relleno = PKCS7(algorithms.AES.block_size).padder()
    relleno_datos = relleno.update(enClaroAux) + relleno.finalize()

    backend = default_backend()
    cifrado = Cipher(algorithms.AES(clave), modes.CBC(iv), backend=backend)

    encriptar = cifrado.encryptor()
    texto_cifrado = encriptar.update(relleno_datos) + encriptar.finalize()

    texto_cifrado_hex = binascii.hexlify(texto_cifrado)
    enString = texto_cifrado_hex.decode('utf-8')
    print("Mensaje cifrado:", enString)


def decodificar(codificado, clave, iv):
    backend = default_backend()
    cifrado = Cipher(algorithms.AES(clave), modes.CBC(iv), backend=backend)
    desencriptar = cifrado.decryptor()

    codificadoAux = binascii.unhexlify(codificado)

    desencriptar_relleno_datos = desencriptar.update(codificadoAux) + desencriptar.finalize()

    quitar_relleno = PKCS7(algorithms.AES.block_size).unpadder()
    decodificacion = quitar_relleno.update(desencriptar_relleno_datos) + quitar_relleno.finalize()

    enString = decodificacion.decode('utf-8')
    print("Mensaje descifrado:", enString)


if __name__ == '__main__':
    clave = b"SeguridadInforma"[:16]
    iv = b"SeguridadInforma"[:16]
    print("1.Cifrar")
    print("2.Descifrar")
    op = int(input())
    if op == 1:
        enClaro = str(input())
        enClaroAux = bytes(enClaro, "utf-8")
        codificar(enClaroAux, clave, iv)

    elif op == 2:
        codificado = str(input())
        decodificar(codificado, clave, iv)

