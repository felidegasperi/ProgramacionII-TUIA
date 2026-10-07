#Clase point
class Point:
    #init es el constructor de la clase, donde definimos los atributos que va a tener
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return '(' + str(self.x) + ',' + str(self.y) + ')'


    def __eq__(self, other) -> bool:
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y


    def __add__(self, other: 'Point') -> 'Point':
        return Point(self.x + other.x, self.y + other.y)

#Clase rectangulo
class Rectangle:
    def __init__(self, width: float, height: float, corner: Point) -> None:
        self.width = width
        self.height = height
        self.corner = corner

# Funcion en version pura
    def mover_rectangulo_vPura(rect: Rectangle, dx: float, dy:float) -> Rectangle:
        rect2 = Rectangle(rect.width, rect.height, Point(rect.corner.x + dx, rect.corner.y + dy))
        return rect2

# Funcion en version modificadora
    def mover_Rectangulo_vModificadora(rect: Rectangle, dx: float, dy:float) -> None:
        rect.corner.x += dx
        rect.corner.y += dy

