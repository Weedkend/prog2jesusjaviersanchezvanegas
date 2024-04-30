import tkinter as tk 
from tkinter import messagebox

def registrar():
    mensaje = f"Nombre: {cnombre.get()}\nApellido: {capellido.get()}\nEdad: {cedad.get()}\nDirección: {cdireccion.get()}\nSexo: {elige_genero.get()}\nTeléfono: {ctelefono.get()}\nCiudad: {selecciona_ciudad.get()}"
    messagebox.showinfo("Datos registrados", mensaje)

ventana=tk.Tk()
ventana.title("Tecnar App")
ventana.geometry("800x800")
ventana.resizable(True,True)

lnombre=tk.Label(ventana,text="Nombre:" )
lnombre.grid(row = 0, column = 17, pady = 4)
cnombre=tk.Entry(ventana, width=30)
cnombre.grid(row = 1, column = 17, pady = 4)

lapellido=tk.Label(ventana,text="Apellido:" )
lapellido.grid(row = 3, column = 17, pady = 4)
capellido=tk.Entry(ventana, width=30)
capellido.grid(row = 4, column = 17, pady = 4)

ledad=tk.Label(ventana,text="Edad:" )
ledad.grid(row = 5, column = 17, pady = 4)
cedad=tk.Entry(ventana, width=30)
cedad.grid(row = 6, column = 17, pady = 4)

ldireccion=tk.Label(ventana,text="Direccion:")
ldireccion.grid(row = 7, column= 17, pady= 4)
cdireccion=tk.Entry(ventana, width=30)
cdireccion.grid(row = 8, column = 17, pady = 4)

lsexo=tk.Label(ventana,text="Sexo:")
lsexo.grid(row = 9, column= 17, pady= 4)
elige_genero = tk.StringVar()

tk.Radiobutton(ventana, text="Masculino", variable=elige_genero, value="Masculino").grid(row=10, column=17, pady=4)
tk.Radiobutton(ventana, text="Femenino", variable=elige_genero, value="Femenino").grid(row=11, column=17, pady=4)

ltelefono=tk.Label(ventana,text="Telefono:")
ltelefono.grid(row=12, column=17, pady=4)
ctelefono=tk.Entry(ventana, width=30)
ctelefono.grid(row=13, column=17, pady=4)

lciudad=tk.Label(ventana,text="Ciudad:")
lciudad.grid(row=14, column=17, pady=4)

selecciona_ciudad = tk.StringVar()

ciudades = ["Bogotá", "Medellín", "Cali", "Barranquilla", "Cartagena"]

ciudad_lista = tk.Listbox(ventana, height=5)
ciudad_lista.grid(row=15, column=17, pady=4)
for ciudad in ciudades:
    ciudad_lista.insert(tk.END, ciudad)

def on_select(event):
    selecciona_ciudad.set(event.widget.get(event.widget.curselection()))

ciudad_lista.bind('<<ListboxSelect>>', on_select)

Registrar = tk.Button(ventana, text="Registrar", command=registrar)
Registrar.grid(row = 16, column = 1, pady = 4)

ventana.mainloop()
