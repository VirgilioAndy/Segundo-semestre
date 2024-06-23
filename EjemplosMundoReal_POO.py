class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def calcular_salario(self):
        return self.salario

class Gerente(Empleado):
    def __init__(self, nombre, salario, bono):
        super().__init__(nombre, salario)
        self.bono = bono

    def calcular_salario(self):
        salario_base = super().calcular_salario()
        return salario_base + self.bono

# Ejemplo de uso
empleado1 = Empleado("Juan", 300)
gerente1 = Gerente("Pedro", 500, 50)

print(f"Salario de {empleado1.nombre}: ${empleado1.calcular_salario()}")
print(f"Salario de {gerente1.nombre}: ${gerente1.calcular_salario()}")
