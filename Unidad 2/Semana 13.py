import tkinter as tk
from tkinter import messagebox

def agregar_dato():
    dato = entry_dato.get()
    if dato:
        listbox_datos.insert(tk.END, dato)
        entry_dato.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "El campo de texto está vacío")

def limpiar_datos():
    listbox_datos.delete(0, tk.END)
    entry_dato.delete(0, tk.END)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación de Datos")

# Crear y colocar los componentes
etiqueta = tk.Label(ventana, text="Ingrese un dato:")
etiqueta.pack(pady=10)

entry_dato = tk.Entry(ventana)
entry_dato.pack(pady=5)

boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato)
boton_agregar.pack(pady=5)

boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_datos)
boton_limpiar.pack(pady=5)

listbox_datos = tk.Listbox(ventana)
listbox_datos.pack(pady=10, fill=tk.BOTH, expand=True)

# Ejecutar el bucle principal
ventana.mainloop()
