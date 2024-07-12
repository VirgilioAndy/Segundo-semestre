class Archivo:
    def __init__(self, nombre):
        """
        Constructor de la clase Archivo.
        Se llama automáticamente al crear una instancia de la clase.

        Parámetros:
        nombre (str): El nombre del archivo que se abrirá.
        """
        self.nombre = nombre
        self.archivo = open(nombre, 'w')
        print(f"Archivo '{self.nombre}' abierto.")

    def escribir(self, contenido):
        """
        Método para escribir contenido en el archivo.

        Parámetros:
        contenido (str): El contenido que se escribirá en el archivo.
        """
        self.archivo.write(contenido)
        print(f"Escrito en el archivo '{self.nombre}': {contenido}")

    def __del__(self):
        """
        Destructor de la clase Archivo.
        Se llama automáticamente cuando todas las referencias al objeto se eliminan.
        Aquí se cierran los recursos abiertos.
        """
        self.archivo.close()
        print(f"Archivo '{self.nombre}' cerrado.")


# Demostración del uso de la clase Archivo

# Creación de una instancia de la clase Archivo (llama al constructor __init__)
archivo = Archivo('mi_archivo.txt')

# Escritura de contenido en el archivo
archivo.escribir("Hola, este es un archivo grande.\n")

# Eliminación de la referencia al objeto archivo (llama al destructor __del__)
del archivo

# En este punto, el destructor __del__ debería haberse llamado, cerrando el archivo.