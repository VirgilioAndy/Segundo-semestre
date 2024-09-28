import tkinter as tk
from tkinter import messagebox


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")

        # Campo de entrada para las tareas
        self.task_entry = tk.Entry(root, width=30)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)
        self.task_entry.bind("<Return>", self.add_task_event)  # Añadir con la tecla Enter

        # Botón para añadir tarea
        self.add_button = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        # Lista para mostrar las tareas
        self.task_listbox = tk.Listbox(root, width=50, height=10, selectmode=tk.SINGLE)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        self.task_listbox.bind("<Double-1>", self.mark_as_completed_event)  # Doble clic para marcar como completada

        # Botón para marcar tarea como completada
        self.complete_button = tk.Button(root, text="Marcar como Completada", command=self.mark_as_completed)
        self.complete_button.grid(row=2, column=0, padx=10, pady=10)

        # Botón para eliminar tarea
        self.delete_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.grid(row=2, column=1, padx=10, pady=10)

    # Función para añadir tarea
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "No se puede añadir una tarea vacía.")

    # Permitir añadir tarea con la tecla Enter
    def add_task_event(self, event):
        self.add_task()

    # Función para marcar tarea como completada
    def mark_as_completed(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task = self.task_listbox.get(selected_task_index)
            self.task_listbox.delete(selected_task_index)
            self.task_listbox.insert(tk.END, f"{task} - Completada")
        else:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea.")

    # Permitir marcar como completada con doble clic
    def mark_as_completed_event(self, event):
        self.mark_as_completed()

    # Función para eliminar tarea
    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.task_listbox.delete(selected_task_index)
        else:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea.")


# Crear la ventana principal
root = tk.Tk()
app = TodoApp(root)
root.mainloop()
