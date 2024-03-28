# Encryption using RSA and AES

from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

# generate keys
key = RSA.generate(2048)
private_key = key
public_key = key.public_key()

# print key
print(private_key.export_key())
print(public_key.export_key())

# generate key file (PEM)
file = open('llaveTumbada.pem', 'wb')
file.write(key.export_key('PEM'))

# RSA encryption
data = 'natalover, arriba los coritdos tumbados'.encode()
# a private key will be used in AES (16 bytes)
# used by a transmitter and the receiver (will be exchanged by both)
session_key = get_random_bytes(16)

print('session_key: ', session_key)

# encrypt the session key with the RSA public key
# use the public key to encrypt
encrypt_rsa = PKCS1_OAEP.new(public_key)
# encrypted version of the session key
encrypt_session_key = encrypt_rsa.encrypt(session_key)
print('encrypt_session_key: ', encrypt_session_key)

# encrypt the data with the AES session key
cipher_aes = AES.new(session_key, AES.MODE_EAX)
# use of a hash to authenticate
# the cipher text is generated with AES
cypther_text, tag = cipher_aes.encrypt_and_digest(data)
nonce = cipher_aes.nonce
print('cypther_text: ', cypther_text)
print('tag: ', tag)

# decrypt using RSA
# the receiver requires the private key to decrypt the session key
decrypt_rsa = PKCS1_OAEP.new(private_key)
session_key = decrypt_rsa.decrypt(encrypt_session_key)

decrypt_aes = AES.new(session_key, AES.MODE_EAX, nonce=nonce)
plain_text = decrypt_aes.decrypt_and_verify(cypther_text, tag)
print('plain_text: ', plain_text)