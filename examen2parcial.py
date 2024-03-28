# import the DES module from the Crypto.Cipher module
from Crypto.Cipher import DES
# use padding to ensure that our messages are a multiple of 8 bytes
from Crypto.Util.Padding import pad
# use unpad to remove the padding from the decrypted message
from Crypto.Util.Padding import unpad
# the next two modules are used to generate random bytes
from Crypto.Random import get_random_bytes
import binascii

llave= b'corridos'  # 8 bytes key

cifrado = DES.new(llave, DES.MODE_CBC)

iv = cifrado.iv

# Get the message from the user
mensaje = input("Please enter the message you want to encrypt: ").encode()

mensajeCifrado = cifrado.encrypt(pad(mensaje, cifrado.block_size))

# Print the encrypted message
print("Encrypted message: ", binascii.hexlify(mensajeCifrado).decode())