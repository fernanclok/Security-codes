#importar la libreria pycryptodome
from Crypto.Cipher import DES
#utilizar padding para compensar bloques menores a 64 bits
from Crypto.Util.Padding import pad
#utilizar unpad para remover el pad al desencriptar el mensaje
from Crypto.Util.Padding import unpad
#el siguiente comando nos permitira agregar un numero aleatorio
from Crypto.Random import get_random_bytes
import binascii

llave= b'corridos'  # 8 bytes key

cifrado = DES.new(llave, DES.MODE_CBC)
print(cifrado.iv) 
print(cifrado.block_size)

iv = cifrado.iv

mensaje = b'Corridos Tumbados'
print(pad(mensaje, cifrado.block_size))
print(mensaje)

mensajeCifrado = cifrado.encrypt(pad(mensaje, cifrado.block_size))
print(mensajeCifrado)

#desencriptar
desencriptar = DES.new(llave, DES.MODE_CBC,iv)

mensajeOriginal = desencriptar.decrypt(mensajeCifrado)
mensajeOriginal = unpad(mensajeOriginal, DES.block_size)
print(mensajeOriginal.decode())

print(binascii.hexlify(mensajeCifrado))