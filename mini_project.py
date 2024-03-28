#  mini project using OTP (One Time Pad) and tkinter (GUI) to create a login system with encryption and decryption options using OTP.
#  The user will be able to create an account, login, encrypt and decrypt messages using OTP.

# the login uses hash to store the user and password in a secure way.

import tkinter as tk
from tkinter import simpledialog, messagebox
from hashlib import md5
import random
import string

# Hash de la contraseña almacenado
passwordEncript = None
userEncript = None

def random_key(length):
    return ''.join(str(random.randint(0, 9)) for _ in range(length))

def otp_encrypt(message, key):
    # Generate a random pad of the same length as the message
    pad = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(len(message)))
    encrypted_message = ''.join(chr(ord(m)^ord(p)) for m,p in zip(message, pad))
    return pad, encrypted_message

def otp_decrypt(encrypted_message, key):
    decrypted_message = ''
    for i in range(len(encrypted_message)):
        char = encrypted_message[i]
        if char.isalpha():
            char_position = ord(char.upper()) - ord('A')
            key_position = int(key[i])
            decrypted_char = chr((char_position - key_position) % 26 + ord('A'))
            if char.islower():
                decrypted_char = decrypted_char.lower()
            decrypted_message += decrypted_char
        else:
            decrypted_message += char
    return decrypted_message

def create_account():
    global userEncript, passwordEncript
    usertext = simpledialog.askstring("Crea tu usuario", "Crea tu usuario")
    text = simpledialog.askstring("Crea tu contraseña", "Crea tu contraseña", show='*')
    userEncript = md5(usertext.encode()).hexdigest()
    passwordEncript = md5(text.encode()).hexdigest()
    messagebox.showinfo("Cuenta", "Cuenta creada exitosamente.")

def login():
    global userEncript, passwordEncript
    if userEncript is None or passwordEncript is None:
        messagebox.showinfo("Error", "Necesitas crear una cuenta primero.")
    else:
        usertext = simpledialog.askstring("Ingresa tu usuario", "Ingresa tu usuario")
        text = simpledialog.askstring("Ingresa tu contraseña", "Ingresa tu contraseña", show='*')
        user = md5(usertext.encode()).hexdigest()
        password = md5(text.encode()).hexdigest()
        if password == passwordEncript and user == userEncript:
            messagebox.showinfo("Acceso", "Acceso concedido")
            encryption()
        else:
            messagebox.showinfo("Acceso", "Acceso denegado")

def decryption():
    decryption_option = simpledialog.askinteger("Seleccione una opción", "1. Descifrar con OTP\n2. Salir")
    if decryption_option == 1:
        # OTP decryption
        encrypted_message = simpledialog.askstring("Ingrese el mensaje cifrado", "Ingrese el mensaje cifrado")
        key = simpledialog.askstring("Ingrese la clave", "Ingrese la clave")
        decrypted_message = otp_decrypt(encrypted_message, key)
        messagebox.showinfo("Mensaje Descifrado", decrypted_message)
    elif decryption_option == 2:
        # Exit
        return
    else:
        messagebox.showinfo("Error", "Opción inválida. Por favor, intenta de nuevo.")
        decryption()

def encryption():
    encryption_option = simpledialog.askinteger("Seleccione una opción", "1. Cifrar con OTP\n2. Descifrar\n3. Salir")
    if encryption_option == 1:
        # OTP encryption
        mensaje = simpledialog.askstring("Ingresa el mensaje que quieres cifrar", "Ingresa el mensaje que quieres cifrar")
        key = random_key(len(mensaje))
        mensajeCifrado = ''
        for i in range(len(mensaje)):
            char = mensaje[i]
            if char.isalpha():
                char_position = ord(char.upper()) - ord('A')
                key_position = int(key[i])
                encrypted_char = chr((char_position + key_position) % 26 + ord('A'))
                if char.islower():
                    encrypted_char = encrypted_char.lower()
                mensajeCifrado += encrypted_char
            else:
                mensajeCifrado += char
        messagebox.showinfo("Mensaje cifrado", f"Llave: {key}\nMensaje cifrado: {mensajeCifrado}")
        encryption()
    elif encryption_option == 2:
        # Decryption
        decryption()
    elif encryption_option == 3:
        # Exit
        return
    else:
        messagebox.showinfo("Error", "Opción inválida. Por favor, intenta de nuevo.")
        encryption()

root = tk.Tk()
root.geometry("400x400+250+100")  # Set window size to 800x600 and position at (250, 100)

# Create account button
create_account_button = tk.Button(root, text="Crear cuenta", command=create_account, height=3, width=20)
create_account_button.place(relx=0.5, rely=0.4, anchor='center')  # Place the button at 40% of the window height, centered horizontally

# Login button
login_button = tk.Button(root, text="Iniciar sesión", command=login, height=3, width=20)
login_button.place(relx=0.5, rely=0.6, anchor='center')  # Place the button at 60% of the window height, centered horizontally

root.mainloop()