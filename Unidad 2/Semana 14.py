import tkinter as tk
from tkinter import messagebox, ttk
from tkcalendar import DateEntry  # Asegúrate de instalar tkcalendar

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")

        # Frame para la lista de eventos
        self.frame_lista = ttk.Frame(self.root)
        self.frame_lista.pack(padx=10, pady=10)

        self.tree = ttk.Treeview(self.frame_lista, columns=("Fecha", "Hora", "Descripción"), show='headings')
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack(side=tk.LEFT)

        self.scrollbar = ttk.Scrollbar(self.frame_lista, orient="vertical", command=self.tree.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.configure(yscrollcommand=self.scrollbar.set)

        # Frame para entrada de datos
        self.frame_entrada = ttk.Frame(self.root)
        self.frame_entrada.pack(padx=10, pady=10)

        ttk.Label(self.frame_entrada, text="Fecha:").grid(row=0, column=0)
        self.entry_fecha = DateEntry(self.frame_entrada, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.entry_fecha.grid(row=0, column=1)

        ttk.Label(self.frame_entrada, text="Hora:").grid(row=1, column=0)
        self.entry_hora = tk.Entry(self.frame_entrada)
        self.entry_hora.grid(row=1, column=1)

        ttk.Label(self.frame_entrada, text="Descripción:").grid(row=2, column=0)
        self.entry_desc = tk.Entry(self.frame_entrada)
        self.entry_desc.grid(row=2, column=1)

        # Botones
        ttk.Button(self.root, text="Agregar Evento", command=self.agregar_evento).pack(pady=5)
        ttk.Button(self.root, text="Eliminar Evento Seleccionado", command=self.eliminar_evento).pack(pady=5)
        ttk.Button(self.root, text="Salir", command=self.root.quit).pack(pady=5)

    def agregar_evento(self):
        fecha = self.entry_fecha.get()
        hora = self.entry_hora.get()
        descripcion = self.entry_desc.get()

        if fecha and hora and descripcion:
            self.tree.insert("", "end", values=(fecha, hora, descripcion))
            self.entry_hora.delete(0, tk.END)
            self.entry_desc.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor complete todos los campos.")

    def eliminar_evento(self):
        seleccionado = self.tree.selection()
        if seleccionado:
            confirmacion = messagebox.askyesno("Confirmar", "¿Está seguro de que desea eliminar este evento?")
            if confirmacion:
                for item in seleccionado:
                    self.tree.delete(item)
        else:
            messagebox.showwarning("Advertencia", "Seleccione un evento para eliminar.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
