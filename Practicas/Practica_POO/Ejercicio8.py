# Un objeto puede contener a otro objeto como atributo. A esto lo llamamos composición.
# Definí dos clases:
# Motor , con los atributos cilindrada (float) y potencia (int, en caballos de fuerza).
# Auto , con los atributos de tipo Motor .
# Agregá un método 
# marca , modelo y motor. 
# El atributo 
# __str__ a 
# motor es un objeto
# Auto que muestre la marca, el modelo y los datos del
# motor.
# Mostrá que se puede acceder de forma anidada a los atributos del motor desde el
# auto (por ejemplo, 
# auto.motor.potencia ).

class Motor:
    def __init__(self, cilindrada: float, potencia: int) -> None:
        self.cilindrada = cilindrada
        self.potencia = potencia


class Auto:
    def __init__(self, marca: str, modelo: str, motor: Motor) -> None:
        self.marca = marca
        self.modelo = modelo
        self.motor = motor

    def __str__(self) -> str:
        return str(self.marca) + ', ' + str(self.modelo) + ' - Motor ' + str(self.motor.cilindrada) + ', (' + str(self.motor.potencia) + ' HP)'


motor = Motor(1.6, 110)

auto = Auto("Renault", "Sandero", motor)

print(auto.motor.potencia)
print("---------")
print(auto.motor.cilindrada)
print("---------")
print(auto)