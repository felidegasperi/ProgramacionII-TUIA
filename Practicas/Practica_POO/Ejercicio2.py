# Definí una clase Circulo que represente un círculo a partir de un único atributo
# radio .
# Agregá dos métodos que devuelven un número (no lo imprimen), usando estas
# fórmulas:
# area() : devuelve el área del círculo, que se calcula como π · radio².
# perimetro() : devuelve el perímetro (la longitud de la circunferencia), que se
# calcula como 2 · π · radio.
# Podés usar 3.1416 como valor aproximado de π, o importar pi desde el módulo
# math .

import math

class Circulo():
    def __init__(self, radio: float) -> None:
        self.radio = radio

    def area(self) -> float:
        return math.pi * self.radio**2

    def perimetro(self) -> float:
        return 2 * math.pi * self.radio


c = Circulo(10)
print(c.area())
print(c.perimetro())