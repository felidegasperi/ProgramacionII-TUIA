# Definí una clase Cancion con los atributos titulo , artista y duracion (la duración
# en segundos, un entero).
# Agregá el método especial __str__ para que, al imprimir una canción, se muestre
# su título, su artista y su duración en formato minutos:segundos . Los segundos deben
# mostrarse siempre con dos dígitos.

class Cancion:
    def __init__(self, titulo: str, artista: str, duracion: int) -> None:
        self.titulo = titulo
        self.artista = artista
        self.duracion = duracion

    def __str__(self) -> str:
        if self.duracion >= 60:
            minutos = self.duracion // 60
            segundos = self.duracion % 60
        else:
            minutos = 0
            segundos = self.duracion

        if segundos < 10:
            return '('+ str(self.titulo) +' - '+ str(self.artista) + ', '+ str(minutos) + ':'+ '0' +  str(segundos) + ')'

        return '('+ str(self.titulo) +' - '+ str(self.artista) + ', '+ str(minutos) + ':'+ str(segundos) +')'

cancion = Cancion("Bohemia Rhapsody", "Queen", 64)

print(cancion)
