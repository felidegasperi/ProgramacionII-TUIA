#Definí una clase Libro que represente un libro. Al crear un libro, se deben poder
#indicar los siguientes atributos:
#titulo (string)
#autor (string)
#anio (int) — año de publicación
#paginas (int) — cantidad de páginas
#Por ahora la clase solo debe tener su constructor. No hace falta agregar ningún
#método todavía.

class Libro:
    def __init__(self, titulo: str, autor: str, anio: int, paginas: int) -> None:
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.paginas = paginas


libro_1 = Libro("El nombre del viento", "Patrick Rothfuss", 2007, 662)

print(libro_1.titulo)
print(libro_1.autor)
print(libro_1.paginas)
