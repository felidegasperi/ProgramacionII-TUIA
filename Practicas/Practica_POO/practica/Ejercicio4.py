# Definí una clase Bateria que represente la batería de un dispositivo. La batería
# tiene un atributo nivel que va de 0 a 100 y que, si no se indica al crearla, arranca
# en 100.
# Agregá los siguientes métodos:
# cargar(cantidad) : aumenta el nivel de la batería en cantidad . El nivel nunca
# puede superar 100 (si se pasa, queda en 100).
# usar(cantidad) : disminuye el nivel de la batería en cantidad . El nivel nunca
# puede ser menor a 0. Si se intenta usar más de lo disponible, debe mostrar el
# mensaje "Batería insuficiente" y dejar el nivel sin cambios.
# Estos métodos modifican el estado del objeto.

class Bateria:
    def __init__(self, nivel: int = 100) -> None:

        if nivel > 100:
            raise ValueError("El nivel de la bateria no puede ser mas de 100")
        
        self.nivel = nivel

    def cargar(self, cantidad: int) -> int:
        if cantidad + self.nivel > 100:
            return 100
        return cantidad + self.nivel

    def usar(self, cantidad: int) -> str:
        if self.nivel - cantidad < 0:
            return "Bateria insuficiente"
        return str(self.nivel - cantidad)

bateria1 = Bateria(70)

print(bateria1.cargar(10))