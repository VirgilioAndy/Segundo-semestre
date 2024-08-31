import json


class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        return self.id

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
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"


class Inventario:
    def __init__(self):
        self.productos = {}  # Diccionario para almacenar productos por ID

    def añadir_producto(self, producto):
        if producto.get_id() in self.productos:
            print("El producto con este ID ya existe.")
        else:
            self.productos[producto.get_id()] = producto
            print("Producto añadido correctamente.")

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
            print("Producto eliminado correctamente.")
        else:
            print("Producto no encontrado.")

    def actualizar_cantidad(self, id, cantidad):
        if id in self.productos:
            self.productos[id].set_cantidad(cantidad)
            print("Cantidad actualizada correctamente.")
        else:
            print("Producto no encontrado.")

    def actualizar_precio(self, id, precio):
        if id in self.productos:
            self.productos[id].set_precio(precio)
            print("Precio actualizado correctamente.")
        else:
            print("Producto no encontrado.")

    def buscar_producto_por_nombre(self, nombre):
        encontrados = [prod for prod in self.productos.values() if nombre.lower() in prod.get_nombre().lower()]
        if encontrados:
            for producto in encontrados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_todos_productos(self):
        if self.productos:
            for producto in self.productos.values():
                print(producto)
        else:
            print("No hay productos en el inventario.")

    def guardar_a_archivo(self, archivo):
        with open(archivo, 'w') as f:
            productos_data = {id: vars(prod) for id, prod in self.productos.items()}
            json.dump(productos_data, f)
        print("Inventario guardado en archivo.")

    def cargar_desde_archivo(self, archivo):
        try:
            with open(archivo, 'r') as f:
                productos_data = json.load(f)
                self.productos = {id: Producto(**data) for id, data in productos_data.items()}
            print("Inventario cargado desde archivo.")
        except FileNotFoundError:
            print("Archivo no encontrado. Se creará un nuevo archivo al guardar.")


def mostrar_menu():
    print("\n--- Menú de Inventario ---")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar cantidad")
    print("4. Actualizar precio")
    print("5. Buscar producto por nombre")
    print("6. Mostrar todos los productos")
    print("7. Guardar inventario en archivo")
    print("8. Cargar inventario desde archivo")
    print("9. Salir")


def main():
    inventario = Inventario()
    archivo = "inventario.json"

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == '1':
            id = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad del producto: "))
            precio = float(input("Precio del producto: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == '2':
            id = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id)

        elif opcion == '3':
            id = input("ID del producto a actualizar cantidad: ")
            cantidad = int(input("Nueva cantidad: "))
            inventario.actualizar_cantidad(id, cantidad)

        elif opcion == '4':
            id = input("ID del producto a actualizar precio: ")
            precio = float(input("Nuevo precio: "))
            inventario.actualizar_precio(id, precio)

        elif opcion == '5':
            nombre = input("Nombre del producto a buscar: ")
            inventario.buscar_producto_por_nombre(nombre)

        elif opcion == '6':
            inventario.mostrar_todos_productos()

        elif opcion == '7':
            inventario.guardar_a_archivo(archivo)

        elif opcion == '8':
            inventario.cargar_desde_archivo(archivo)

        elif opcion == '9':
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Por favor, elige una opción del menú.")


if __name__ == "__main__":
    main()
