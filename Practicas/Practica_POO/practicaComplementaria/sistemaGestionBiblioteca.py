#Ejercicio 1
class Libro:
    def __init__(self, 
                 codigo_libro: str, 
                 titulo: str,
                 autor: str) -> None:
        self.codigo_libro = codigo_libro
        self.titulo = titulo
        self.autor = autor

    def __str__(self) -> str:
        return 'Codigo del libro: ' + self.codigo_libro + ' \n Titulo: ' + self.titulo + '\n Autor: ' + self.autor

novela1 = Libro("N001",
            "Cien años de soledad",
            "Gabriel Garcia Marquez")

#print(novela1)

#Ejercicio 2
class Ejemplares:
    def __init__(self,
                 libro: Libro,
                 total: int,
                 prestados: int = 0) -> None:
        self.libro = libro
        self.total = total
        self.prestados = prestados

#Ejercicio 3
    def disponibles(self) -> int:
        return self.total

#Ejercicio 4
    def prestar(self, cantidad: int) -> None:
        if cantidad <= 0 or cantidad > self.total:
            return print("La cantidad de ejemplares a prestar no esta disponible")
        self.prestados = self.prestados + cantidad
        self.total = self.total - cantidad


    def devolver(self, cantidad: int) -> None:
        if cantidad <= 0 or cantidad > self.prestados:
            return print("La cantidad de ejemplares a devolver no esta disponible")
        self.total = self.total + cantidad
        self.prestados = self.prestados - cantidad

#Ejercicio 5
    def agregar_ejemplares(self, cantidad: int) -> None:
        if cantidad <= 0:
            return print("La cantidad de ejemplares a agregar es incorrecta")
        self.total = self.total + cantidad

ejemplar_novela1 = Ejemplares(novela1, 5)

#Ejercicio 6 A empezar
class Biblioteca:
    def __init__(self) -> None:
        ejemplares = {}

#ejemplar_novela1.prestar(2)
#ejemplar_novela1.prestar(1)

#print(ejemplar_novela1.disponibles())

#ejemplar_novela1.devolver(1)

#print(ejemplar_novela1.disponibles())

#ejemplar_novela1.agregar_ejemplares(3)