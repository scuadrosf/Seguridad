from Crypto.Cipher import AES
import binascii

# Clave y IV
key = b'SeguridadInforma'
iv = b'SeguridadInforma'

# Texto cifrado
ciphertext = binascii.unhexlify('9bc43d7ec1aa11f64302287b17be9f7b')

# Crear objeto cifrador AES
cipher = AES.new(key, AES.MODE_CBC, iv)

# Descifrar texto y eliminar padding
plaintext = cipher.decrypt(ciphertext).rstrip(b"\0")

# Imprimir resultado
print("Texto descifrado: ", plaintext.decode())
