# Definí una clase Usuario que represente al usuario de un servicio de almacenamiento en la nube, con los atributos nombre y espacio_base (los GB incluidos). 
# Agregá un método espacio_total() que devuelva el espacio_base .
# Definí una subclase UsuarioPremium que herede de Usuario .
# Un usuario premium, además del espacio base, tiene un espacio_extra .
# Al escribir el constructor de
# UsuarioPremium :
# Usá super().__init__(...) para inicializar el reutilizando el constructor de la clase padre.
# Agregá el nuevo atributo 
# Redefiní ( override ) el método nombre y el espacio_extra .
# espacio_base
# espacio_total() en 
# UsuarioPremium para que
# devuelva el espacio base más el espacio extra

class Usuario:
    def __init__(self, nombre: str, espacio_base: int) -> None:
        self.nombre = nombre
        self.espacio_base = espacio_base

    def espacio_total(self) -> int:
        return self.espacio_base


class UsuarioPremium(Usuario):
    def __init__(self, nombre: str, espacio_base: int, espacio_extra: int) -> None:
        super().__init__(nombre, espacio_base)
        self.espacio_extra = espacio_extra

    def espacio_total(self) -> int:
        return super().espacio_total() + self.espacio_extra


# comprobacion de lo realizado

u = Usuario("Ana", 15)
print(u.espacio_total())
print("-----------")

p = UsuarioPremium("Bruno", 15, 100)
print(p.espacio_total())
print(p.nombre)


    