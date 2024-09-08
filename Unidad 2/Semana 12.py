class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Categoría: {self.categoria}, ISBN: {self.isbn}"


class Usuario:
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id
        self.libros_prestados = []

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        self.libros_prestados.remove(libro)

    def listar_libros_prestados(self):
        return [str(libro) for libro in self.libros_prestados]

    def __str__(self):
        return f"Nombre: {self.nombre}, ID: {self.user_id}"


class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.usuarios = set()

    def añadir_libro(self, libro):
        if libro.isbn in self.libros:
            print(f"El libro con ISBN {libro.isbn} ya está en la biblioteca.")
        else:
            self.libros[libro.isbn] = libro
            print(f"Libro añadido: {libro}")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} eliminado de la biblioteca.")
        else:
            print(f"No se encontró el libro con ISBN {isbn}.")

    def registrar_usuario(self, nombre, user_id):
        if user_id in {u.user_id for u in self.usuarios}:
            print(f"El usuario con ID {user_id} ya está registrado.")
        else:
            usuario = Usuario(nombre, user_id)
            self.usuarios.add(usuario)
            print(f"Usuario registrado: {usuario}")

    def dar_baja_usuario(self, user_id):
        usuario = next((u for u in self.usuarios if u.user_id == user_id), None)
        if usuario:
            self.usuarios.remove(usuario)
            print(f"Usuario con ID {user_id} dado de baja.")
        else:
            print(f"No se encontró el usuario con ID {user_id}.")

    def prestar_libro(self, isbn, user_id):
        libro = self.libros.get(isbn)
        usuario = next((u for u in self.usuarios if u.user_id == user_id), None)
        if libro and usuario:
            usuario.prestar_libro(libro)
            del self.libros[isbn]
            print(f"Libro prestado a {usuario.nombre}: {libro}")
        else:
            print(f"Error al prestar libro: Libro o usuario no encontrado.")

    def devolver_libro(self, isbn, user_id):
        libro = next((l for l in self.libros.values() if l.isbn == isbn), None)
        usuario = next((u for u in self.usuarios if u.user_id == user_id), None)
        if libro and usuario:
            usuario.devolver_libro(libro)
            self.libros[isbn] = libro
            print(f"Libro devuelto por {usuario.nombre}: {libro}")
        else:
            print(f"Error al devolver libro: Libro o usuario no encontrado.")

    def buscar_libro(self, criterio, valor):
        resultado = [str(libro) for libro in self.libros.values() if getattr(libro, criterio) == valor]
        if resultado:
            return "\n".join(resultado)
        else:
            return "No se encontraron libros con ese criterio."

    def listar_libros_prestados(self, user_id):
        usuario = next((u for u in self.usuarios if u.user_id == user_id), None)
        if usuario:
            return usuario.listar_libros_prestados()
        else:
            return f"No se encontró el usuario con ID {user_id}."


# Prueba del sistema
if __name__ == "__main__":
    biblioteca = Biblioteca()

    # Añadir libros
    libro1 = Libro("El Principito", "Antoine de Saint-Exupéry", "Infantil", "123456")
    libro2 = Libro("1984", "George Orwell", "Ficción", "654321")
    biblioteca.añadir_libro(libro1)
    biblioteca.añadir_libro(libro2)

    # Registrar usuarios
    biblioteca.registrar_usuario("Juan Pérez", "u001")
    biblioteca.registrar_usuario("María Gómez", "u002")

    # Prestar libro
    biblioteca.prestar_libro("123456", "u001")

    # Buscar libros
    print(biblioteca.buscar_libro("titulo", "1984"))

    # Listar libros prestados
    usuario_prestado = next(u for u in biblioteca.usuarios if u.user_id == "u001")
    print(usuario_prestado.listar_libros_prestados())

    # Devolver libro
    biblioteca.devolver_libro("123456", "u001")

    # Quitar libro
    biblioteca.quitar_libro("654321")

    # Dar de baja usuario
    biblioteca.dar_baja_usuario("u002")
