from abc import ABC, abstractmethod

# Abstracción
class Vehiculo(ABC):
    def __init__(self, marca, modelo, año):
        self._marca = marca  # Encapsulación: atributos privados
        self._modelo = modelo
        self._año = año

    # Métodos de acceso y modificación (Encapsulación)
    def get_marca(self):
        return self._marca

    def set_marca(self, marca):
        self._marca = marca

    def get_modelo(self):
        return self._modelo

    def set_modelo(self, modelo):
        self._modelo = modelo

    def get_año(self):
        return self._año

    def set_año(self, año):
        self._año = año

    @abstractmethod
    def moverse(self):
        pass

# Herencia
class Carro(Vehiculo):
    def __init__(self, marca, modelo, año, numero_puertas):
        super().__init__(marca, modelo, año)
        self._numero_puertas = numero_puertas

    def get_numero_puertas(self):
        return self._numero_puertas

    def set_numero_puertas(self, numero_puertas):
        self._numero_puertas = numero_puertas

    # Polimorfismo
    def moverse(self):
        return f"El carro {self._marca} {self._modelo} se está moviendo en la carretera."

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, año, tipo):
        super().__init__(marca, modelo, año)
        self._tipo = tipo  # Encapsulación: atributo privado

    def get_tipo(self):
        return self._tipo

    def set_tipo(self, tipo):
        self._tipo = tipo

    # Polimorfismo
    def moverse(self):
        return f"La motocicleta {self._marca} {self._modelo} está avanzando en la pista."

# Uso del polimorfismo
def probar_vehiculos(vehiculo):
    print(vehiculo.moverse())

# Creación de instancias de Carro y Motocicleta
carro = Carro("Toyota", "Corolla", 2021, 4)
motocicleta = Motocicleta("Yamaha", "R1", 2020, "Deportiva")

# Probar los métodos polimórficos
probar_vehiculos(carro)
probar_vehiculos(motocicleta)