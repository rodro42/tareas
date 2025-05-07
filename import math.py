import math
#Hoja de trabajo 11-Laboratorio
# Clase base
class ExperimentoFisico:
    pass

# Subclase CaidaLibre
class CaidaLibre(ExperimentoFisico):
    def __init__(self, altura, gravedad=9.81):
        if altura < 0:
            raise ValueError("La altura no puede ser negativa.")
        if gravedad == 0:
            raise ValueError("La gravedad no puede ser cero.")
        self.altura = altura
        self.gravedad = gravedad

    def calcular_tiempo_caida(self):
        # Fórmula: t = sqrt(2 * h / g)
        tiempo = math.sqrt(2 * self.altura / self.gravedad)
        return tiempo

# Ejemplo de uso
try:
    experimento = CaidaLibre(altura=20)  # puedes cambiar la altura
    tiempo = experimento.calcular_tiempo_caida()
    print(f"El tiempo de caída es: {tiempo:.2f} segundos.")
except ValueError as e:
    print(f"Error: {e}")