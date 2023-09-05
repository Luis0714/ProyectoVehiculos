import time
import random

# Decorador para agregar características especiales
def turbo_decorator(vehicle_class):
    class TurboVehicle(vehicle_class):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.is_turbo_enabled = False

        def enable_turbo(self):
            self.is_turbo_enabled = True

        def disable_turbo(self):
            self.is_turbo_enabled = False

        def acelerar(self, velocidad):
            if self.is_turbo_enabled:
                velocidad *= 1.5  # Aumenta la velocidad con turbo
            super().acelerar(velocidad)

    return TurboVehicle

# Clase base Vehiculo
class Vehiculo:
    def __init__(self, velocidad_maxima, capacidad_gasolina):
        self.velocidad_maxima = velocidad_maxima
        self.capacidad_gasolina = capacidad_gasolina
        self.velocidad_actual = 0
        self.gasolina_actual = capacidad_gasolina

    def acelerar(self, velocidad):
        if self.gasolina_actual > 0:
            if velocidad > self.velocidad_maxima:
                velocidad = self.velocidad_maxima
            self.velocidad_actual = velocidad
            self.gasolina_actual -= 1
            print(f"{self.__class__.__name__}: Acelerando a {self.velocidad_actual} km/h")
        else:
            print(f"{self.__class__.__name__}: Sin gasolina")

    def frenar(self):
        self.velocidad_actual = 0
        print(f"{self.__class__.__name__}: Frenando")

    def cargar_gasolina(self, cantidad):
        self.gasolina_actual += cantidad
        if self.gasolina_actual > self.capacidad_gasolina:
            self.gasolina_actual = self.capacidad_gasolina
        print(f"{self.__class__.__name__}: Gasolina recargada. Gasolina actual: {self.gasolina_actual}/{self.capacidad_gasolina}")

# Subclases de Vehiculo
class Coche(Vehiculo):
    pass

class Moto(Vehiculo):
    pass

class Camion(Vehiculo):
    pass

# Crear instancias de vehículos
coche = Coche(180, 50)
moto = Moto(150, 30)
camion = Camion(120, 80)

# Aplicar decorador de Turbo a Coche
@turbo_decorator
class CocheTurbo(Coche):
    pass

coche_turbo = CocheTurbo(200, 50)

# Función para simular una carrera
def simular_carrera(vehiculos, distancia):
    print("¡Comienza la carrera!")
    cronometro_inicio = time.time()
    while True:
        for vehiculo in vehiculos:
            if random.random() < 0.8:  # Probabilidad de acelerar
                velocidad = random.randint(0, vehiculo.velocidad_maxima)
                vehiculo.acelerar(velocidad)
            else:
                vehiculo.frenar()
            if vehiculo.gasolina_actual <= 0:
                print(f"{vehiculo.__class__.__name__} se quedó sin gasolina.")
                vehiculos.remove(vehiculo)
                if not vehiculos:
                    print("¡Todos los vehículos se quedaron sin gasolina! La carrera ha terminado.")
                    return
        tiempo_transcurrido = time.time() - cronometro_inicio
        if tiempo_transcurrido >= distancia / max(vehiculo.velocidad_maxima for vehiculo in vehiculos):
            print("¡Ha terminado la carrera!")
            return

# Simular una carrera con varios tipos de vehículos
simular_carrera([coche, moto, camion, coche_turbo], 1000)
