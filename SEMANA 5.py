import math  # Importa el módulo math para utilizar constantes y funciones matemáticas


# Función para calcular el área de un círculo
def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.

    :param radio: Radio del círculo
    :return: Área del círculo
    """
    return math.pi * (radio ** 2)  # Fórmula: π * radio^2


# Función para calcular el área de un cuadrado
def calcular_area_cuadrado(lado):
    """
    Calcula el área de un cuadrado dado el tamaño de su lado.

    :param lado: Lado del cuadrado
    :return: Área del cuadrado
    """
    return lado * lado  # Fórmula: lado^2


# Función para calcular el área de un triángulo
def calcular_area_triangulo(base, altura):
    """
    Calcula el área de un triángulo dada su base y altura.

    :param base: Base del triángulo
    :param altura: Altura del triángulo
    :return: Área del triángulo
    """
    return (base * altura) / 2  # Fórmula: (base * altura) / 2


# Función principal
def main():
    print("Calculadora de Áreas")  # Imprime el título del programa

    # Solicita el radio y calcula el área del círculo
    radio = float(input("Introduce el radio del círculo: "))
    area_circulo = calcular_area_circulo(radio)
    print(f"El área del círculo es: {area_circulo}")

    # Solicita el lado y calcula el área del cuadrado
    lado = float(input("Introduce el lado del cuadrado: "))
    area_cuadrado = calcular_area_cuadrado(lado)
    print(f"El área del cuadrado es: {area_cuadrado}")

    # Solicita la base y la altura, y calcula el área del triángulo
    base = float(input("Introduce la base del triángulo: "))
    altura = float(input("Introduce la altura del triángulo: "))
    area_triangulo = calcular_area_triangulo(base, altura)
    print(f"El área del triángulo es: {area_triangulo}")


# Punto de entrada del programa
if __name__ == "__main__":
    main()  # Llama a la función principal para ejecutar el programa
