class ClimaDiario:
    def __init__(self):
        self.temperatura = None

    def ingresar_temperatura(self):
        """
        Método para ingresar la temperatura diaria.
        """
        self.temperatura = float(input("Ingrese la temperatura del día: "))

    def obtener_temperatura(self):
        """
        Método para obtener la temperatura diaria.
        """
        return self.temperatura

class ClimaSemana:
    def __init__(self):
        self.clima_diario = [ClimaDiario() for _ in range(7)]  # Lista de objetos ClimaDiario para cada día de la semana

    def ingresar_temperaturas_semana(self):
        """
        Método para ingresar las temperaturas diarias de la semana.
        """
        for dia in range(7):

            self.clima_diario[dia].ingresar_temperatura()

    def calcular_promedio_semanal(self):
        """
        Método para calcular el promedio semanal de temperaturas.
        """
        temperaturas_semana = [clima_diario.obtener_temperatura() for clima_diario in self.clima_diario]
        promedio = sum(temperaturas_semana) / len(temperaturas_semana)
        return promedio

def main():
    clima_semana = ClimaSemana()

    # Ingresar temperaturas de la semana
    clima_semana.ingresar_temperaturas_semana()

    # Calcular el promedio semanal
    promedio = clima_semana.calcular_promedio_semanal()

    # Mostrar el resultado
    print(f"El promedio semanal de temperaturas es: {promedio:.2f} grados Celsius")

if __name__ == "__main__":
    main()
