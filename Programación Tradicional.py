def ingresar_temperaturas_diarias():
    """
    Función para ingresar las temperaturas diarias de la semana.
    Retorna una lista con las temperaturas ingresadas.
    """
    temperaturas = []
    for dia in range(1, 8):
        temperatura = float(input(f"Ingrese la temperatura del día {dia}: "))
        temperaturas.append(temperatura)
    return temperaturas

def calcular_promedio_semanal(temperaturas):
    """
    Función para calcular el promedio semanal de las temperaturas ingresadas.
    Recibe una lista de temperaturas y retorna el promedio.
    """
    if len(temperaturas) == 0:
        return 0
    else:
        return sum(temperaturas) / len(temperaturas)

def main():
    # Obtener las temperaturas diarias
    temperaturas_semana = ingresar_temperaturas_diarias()

    # Calcular el promedio semanal
    promedio = calcular_promedio_semanal(temperaturas_semana)

    # Mostrar el resultado
    print(f"El promedio semanal de temperaturas es: {promedio:.2f} grados Celsius")

if __name__ == "__main__":
    main()
