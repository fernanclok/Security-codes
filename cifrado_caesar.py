def caesar_cipher(text, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ""

    for char in text:
        if char.isupper():
            index = (alphabet.index(char.lower()) + shift) % 26
            result += alphabet[index].upper()
        else:
            index = (alphabet.index(char) + shift) % 26
            result += alphabet[index]

    return result

text = input("Ingrese el texto a cifrar: ")
shift = int(input("Ingrese el desplazamiento: "))

print("Texto : " + text)
print("Desplazamiento : " + str(shift))
print("Cifrado: " + caesar_cipher(text, shift))