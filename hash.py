from hashlib import md5

# hast of the password and user
passwordEncript = "d77ebde4e2f3be84212200bb9a24c7cd"
userEncript = "1c29b41adbcd82d9455088e9ffa8b67b"

# request the user and password
usertext = str(input("Ingresa tu usuario: "))
text = str(input("Ingresa tu contraseña: "))

user = md5(usertext.encode()).hexdigest()
# calculate the hash of the password
password = md5(text.encode()).hexdigest()

# compare the hashes with the stored ones
if password == passwordEncript and user == userEncript:
    print("Acceso concedido")
else:
    print("Acceso denegado")
