def crack_caesar_cipher(text):
    # Calculate the frequency of each letter in the text
    freq = {}
    for char in text:
        if char.isalpha() or char.isspace():
            char_lower = char.lower()
            freq[char_lower] = freq.get(char_lower, 0) + 1

    # obtain the most common letter
    most_common = max(freq, key=freq.get)
    print(f'La letra que más se repite es: {most_common}')

    # calculate the displacement of the most common letter with respect to 'e' (the most common letter in English) 
    desplazamiento = (ord(most_common) - ord('e')) % 26
    print(f'El desplazamiento es: {desplazamiento}')

text = input("Ingresa el texto cifrado: ")
crack_caesar_cipher(text)