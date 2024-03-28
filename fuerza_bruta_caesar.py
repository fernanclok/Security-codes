def caesar_brute_force(ciphertext):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for key in range(len(alphabet)):
        plaintext = ''
        for c in ciphertext:
            if c in alphabet:
                index = (alphabet.find(c) - key) % len(alphabet)
                plaintext += alphabet[index]
            else:
                plaintext += c
        print(f'Key: {key}, Plaintext: {plaintext}')

ciphertext = input("Ingresa el texto cifrado: ")
caesar_brute_force(ciphertext.lower())