import tkinter as tk
from tkinter import messagebox, Listbox, Scrollbar, END

class TareaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas Pendientes")

        # Frame para la entrada y botones
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        # Campo de entrada para nuevas tareas
        self.tarea_entry = tk.Entry(frame, width=40)
        self.tarea_entry.pack(side=tk.LEFT, padx=10)

        # Botón para añadir tarea
        self.add_button = tk.Button(frame, text="Añadir Tarea", command=self.agregar_tarea)
        self.add_button.pack(side=tk.LEFT)

        # Botón para marcar tarea como completada
        self.complete_button = tk.Button(frame, text="Marcar como Completada", command=self.marcar_completada)
        self.complete_button.pack(side=tk.LEFT)

        # Botón para eliminar tarea
        self.delete_button = tk.Button(frame, text="Eliminar Tarea", command=self.eliminar_tarea)
        self.delete_button.pack(side=tk.LEFT)

        # Listbox para mostrar las tareas
        self.tareas_listbox = Listbox(self.root, width=50, height=10, selectmode=tk.SINGLE)
        self.tareas_listbox.pack(pady=20)

        # Scrollbar
        scrollbar = Scrollbar(self.root)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tareas_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.tareas_listbox.yview)

        # Bind de atajos de teclado
        self.root.bind('<Return>', lambda event: self.agregar_tarea())  # Enter
        self.root.bind('<c>', lambda event: self.marcar_completada())  # C
        self.root.bind('<Delete>', lambda event: self.eliminar_tarea())  # Delete
        self.root.bind('<Escape>', lambda event: self.root.quit())  # Escape

    def agregar_tarea(self):
        tarea = self.tarea_entry.get()
        if tarea:  # Verificar que la entrada no esté vacía
            self.tareas_listbox.insert(END, tarea)
            self.tarea_entry.delete(0, END)  # Limpiar el campo de entrada
        else:
            messagebox.showwarning("Advertencia", "Por favor ingresa una tarea.")

    def marcar_completada(self):
        try:
            seleccion = self.tareas_listbox.curselection()[0]
            tarea = self.tareas_listbox.get(seleccion)
            self.tareas_listbox.delete(seleccion)
            self.tareas_listbox.insert(seleccion, tarea + " (Completada)")
            self.tareas_listbox.itemconfig(seleccion, {'bg': 'lightgreen'})  # Cambiar color de fondo
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor selecciona una tarea para marcar como completada.")

    def eliminar_tarea(self):
        try:
            seleccion = self.tareas_listbox.curselection()[0]
            self.tareas_listbox.delete(seleccion)
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor selecciona una tarea para eliminar.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TareaApp(root)
    root.mainloop()
