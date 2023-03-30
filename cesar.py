def cesar(cifrado, desplazamiento):
    descifrado = []
    for caracter in cifrado:
        letra = ord(caracter)
        if caracter.isupper():
            descifrado.append(chr(((letra - ord('A')) - desplazamiento) % 26 + ord('A')))
        else:
            descifrado.append(chr(((letra - ord('a')) - desplazamiento) % 26 + ord('a')))
    return descifrado

if __name__ == '__main__':
    cifrado = str(input())
    for i in range(26):
        descifrado = cesar(cifrado, i)
        print(i+1, end=" ")
        for j in range(len(descifrado)):
            print(descifrado[j], end="")
        print()
