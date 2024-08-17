# Clase Producto
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters y Setters
    def get_id(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f'ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}'

# Clase Inventario
class Inventario:
    def __init__(self):
        self.productos = []

    # Añadir nuevo producto
    def añadir_producto(self, producto):
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("Error: Ya existe un producto con ese ID.")
                return
        self.productos.append(producto)
        print("Producto añadido exitosamente.")

    # Eliminar producto por ID
    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                print("Producto eliminado.")
                return
        print("Error: Producto no encontrado.")

    # Actualizar cantidad o precio de un producto por ID
    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)
                print("Producto actualizado.")
                return
        print("Error: Producto no encontrado.")

    # Buscar productos por nombre
    def buscar_producto(self, nombre_producto):
        productos_encontrados = [p for p in self.productos if nombre_producto.lower() in p.get_nombre().lower()]
        if productos_encontrados:
            for p in productos_encontrados:
                print(p)
        else:
            print("No se encontraron productos con ese nombre.")

    # Mostrar todos los productos
    def mostrar_productos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for p in self.productos:
                print(p)

# Menú interactivo en la consola
def menu():
    inventario = Inventario()

    while True:
        print("\n--- Menú de Gestión de Inventario ---")
        print("1. Añadir nuevo producto")
        print("2. Eliminar producto por ID")
        print("3. Actualizar producto")
        print("4. Buscar productos por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Elija una opción: ")

        if opcion == "1":
            id_producto = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            nuevo_producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.añadir_producto(nuevo_producto)

        elif opcion == "2":
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("Ingrese el ID del producto a actualizar: ")
            nueva_cantidad = input("Ingrese la nueva cantidad (o presione Enter para no cambiar): ")
            nuevo_precio = input("Ingrese el nuevo precio (o presione Enter para no cambiar): ")
            nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else None
            nuevo_precio = float(nuevo_precio) if nuevo_precio else None
            inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio)

        elif opcion == "4":
            nombre_producto = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre_producto)

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            print("Saliendo del sistema de gestión de inventario.")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el menú
if __name__ == "__main__":
    menu()
