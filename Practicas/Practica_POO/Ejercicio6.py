# Definí una clase Color que represente un color en formato RGB, con tres atributos:
# rojo , verde y azul (cada uno un entero de 0 a 255).
# Agregá:
# El método __str__ , para que al imprimir un color se muestre como RGB(r, g,
# b) .
# El método __eq__ , de modo que dos colores se consideren iguales cuando sus
# tres componentes coinciden. Antes de comparar, verificá con isinstance que el
# otro objeto también sea un Color .


class Color:
    def __init__(self, rojo: int, verde: int, azul: int) -> None:
        if not (0 <= rojo <= 255):
            raise ValueError("Rango equivocado")
        if not (0 <= verde <= 255):
            raise ValueError("Rango equivocado")
        if not (0 <= azul <= 255):
            raise ValueError("Rango equivocado")
        
        self.rojo = rojo
        self.verde = verde
        self.azul = azul

    def __str__(self) -> str:
        return 'RGB ('+ str(self.rojo) +' , '+ str(self.verde) + ', '+ str(self.azul) + ')'

    def __eq__(self, other: object) -> bool:
        # condicional para revisar si other es de clase Color
        if not isinstance(other, Color):
            return False
        
        return self.rojo == other.rojo and self.verde == other.verde and self.azul == other.azul


rojo = Color(255, 0, 0)
print(rojo)
print("---------------")

#se crea otro objeto y se compara con el ya existente para ver si son iguales
otro_rojo = Color(255, 0, 0)
print(rojo == otro_rojo)
print("---------------")

#se intenta ver si rojo es otro_rojo
print(rojo is otro_rojo)
print("---------------")

#nos fijamos si azul es igual a rojo
azul = Color(0, 0, 255)
print(rojo == azul)
