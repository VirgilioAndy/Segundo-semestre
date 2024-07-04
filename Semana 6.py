# Definición de la clase base 'Empleado'
class Empleado:
    def __init__(self, nombre, salario_base):
        self.__nombre = nombre  # Encapsulación del atributo nombre
        self.__salario_base = salario_base  # Encapsulación del atributo salario_base

    def get_nombre(self):
        return self.__nombre

    def calcular_salario(self):
        return self.__salario_base


# Definición de la clase derivada 'Desarrollador' que hereda de 'Empleado'
class Desarrollador(Empleado):
    def __init__(self, nombre, salario_base, lenguaje):
        super().__init__(nombre, salario_base)
        self.__lenguaje = lenguaje  # Encapsulación del atributo lenguaje

    def programar(self):
        return f"{self.get_nombre()} está programando en {self.__lenguaje}"

    def calcular_salario(self):
        # Sobrescribe el método calcular_salario para incluir un bono para desarrolladores
        return super().calcular_salario() * 1.2


# Definición de la clase derivada 'Gerente' que hereda de 'Empleado'
class Gerente(Empleado):
    def __init__(self, nombre, salario_base, departamento):
        super().__init__(nombre, salario_base)
        self.__departamento = departamento  # Encapsulación del atributo departamento

    def asignar_tareas(self):
        return f"{self.get_nombre()} está asignando tareas en el departamento {self.__departamento}"

    def calcular_salario(self):
        # Sobrescribe el método calcular_salario para incluir un bono adicional para gerentes
        return super().calcular_salario() * 1.5


# Creación de instancias y uso de los métodos
def main():
    desarrollador1 = Desarrollador("Carlos", 3000, "Python")
    gerente1 = Gerente("Laura", 4000, "Desarrollo")

    # Accediendo a métodos de las clases derivadas
    print(desarrollador1.programar())
    print(f"Salario de {desarrollador1.get_nombre()}: ${desarrollador1.calcular_salario():.2f}")

    print(gerente1.asignar_tareas())
    print(f"Salario de {gerente1.get_nombre()}: ${gerente1.calcular_salario():.2f}")


if __name__ == "__main__":
    main()