import tkinter as tk 
from tkinter import messagebox
from PIL import Image, ImageTk

usuarios = {}

ventana=tk.Tk()
ventana.title("Tecnar App")
ventana.config(bg="sky blue")
ventana.geometry("800x500")
ventana.resizable(False,False)

# Primer frame
frame1 = tk.Frame(ventana, width=400, height=800, relief="raised", bd=1, bg="white")
frame1.grid(row=0, column=0, pady=0)

imagen = Image.open("C:\\Users\\Javier\\Documents\\repositorio-de-git\\login\\R.png")
imagen = imagen.resize((300, 400))
imagen = ImageTk.PhotoImage(imagen)
label = tk.Label(frame1, image=imagen)
label.image = imagen
label.place(relx=0.5, rely=0.3, anchor="center")

frame2 = tk.Frame(ventana, width=300, height=300, relief="raised", bd=1, bg="light grey")
frame2.grid(row=0, column=1, pady=10, padx=10)

def login():
    username = usuario_entry.get()
    password = contrasena_entry.get()
    
    if username == "user" and password == "admin":
        messagebox.showinfo("Login exitoso", "¡Bienvenido!")
    else:
        messagebox.showerror("Error de login", "Nombre de usuario o contraseña incorrecto")

def registrar():
    nuevo_usuario = usuario_entry.get()
    nueva_contrasena = contrasena_entry.get()
    
    if nuevo_usuario in usuarios:
        messagebox.showerror("Error de registro", "El nombre de usuario ya existe")
    else:
        usuarios[nuevo_usuario] = nueva_contrasena
        messagebox.showinfo("Registro exitoso", "¡Usuario registrado con éxito!")


def centrar_contenido():
    frame2.update_idletasks()
    width = frame2.winfo_width()
    height = frame2.winfo_height()
    x = (frame2.winfo_toplevel().winfo_width() - width) / 2
    y = (frame2.winfo_toplevel().winfo_height() - height) / 2
    frame2.place(in_=ventana, relx=0.79, rely=0.5, x=-width/2, y=-height/2)

centrar_contenido()

etiqueta = tk.Label(frame2, text="LOGIN", bg="gray", fg="white", font=("Arial", 16), width=20, height=2, anchor="center")
etiqueta.grid(row=0, column=0, columnspan=2, pady=(10, 20), sticky="n")

usuario_label = tk.Label(frame2, text="Usuario:", bg="lightgrey")
usuario_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

usuario_entry = tk.Entry(frame2)
usuario_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

contrasena_label = tk.Label(frame2, text="Contraseña:", bg="lightgrey")
contrasena_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

contrasena_entry = tk.Entry(frame2, show="*")
contrasena_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

login_button = tk.Button(frame2, text="Iniciar sesión", bg="blue", fg="white", font=("Arial", 12), command=login)
login_button.grid(row=3, column=0, columnspan=2, pady=10)

registro_button = tk.Button(frame2, text="Registrarse", bg="green", fg="white", font=("Arial", 12), command=registrar)
registro_button.grid(row=4, column=0, columnspan=2, pady=5)

ventana.mainloop()