# Recordá que los atributos de clase son compartidos por todas las instancias, mientras que los atributos de instancia son propios de cada objeto. Un buen uso de un atributo de clase es guardar un valor que vale igual para todos los objetos, como una regla o una constante.
# Definí una clase 
# Estudiante que tenga:
# Un atributo de clase nota_para_aprobar , con valor inicial 6 . Es el mismo para
# todos los estudiantes: representa la nota mínima con la que se aprueba.
# Atributos de instancia 
# nombre y notas (una lista de notas, que arranca vacía).
# Un método agregar_nota(nota) que agregue una nota a la lista.
# Un método promedio() que devuelva el promedio de las notas del estudiante (o 0 si todavía no tiene notas).
# Un método aprobo() que devuelva mayor o igual a nota_para_aprobar .
# True cuando el promedio del estudiante es
# Un método de clase (@classmethod ) llamadocambiar_nota_para_aprobar(nueva_nota) que cambie el atributo de clase. Al cambiarlo, la nueva exigencia debe valer para todos los estudiantes.

class Estudiante:
    #atributo de clase
    nota_para_aprobar = 6

    # atributos de instancia 
    def __init__(self, nombre: str, notas: list[float]) -> None:
        self.nombre = nombre
        self.notas = notas

    def agregar_nota(self, nota: float) -> None:
        self.notas.append(nota)

    def promedio(self) -> float:
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)

    def aprobo(self) -> bool:
        return self.promedio() > float(self.nota_para_aprobar)

    @classmethod
    def cambiar_nota_para_aprobar(cls, nueva_nota: int) -> None:
        cls.nota_para_aprobar = nueva_nota


# comprobacion de codigo

a = Estudiante("Ana", [])
a. agregar_nota(6)
a.agregar_nota(7)

print(a.promedio())
print("--------")
print(a.aprobo())

print("-----")

# se utiliza el metodo de clase para modificar el atributo de clase
Estudiante.cambiar_nota_para_aprobar(7)
print(a.aprobo())         # ahora pide nota 7 para aprobar
