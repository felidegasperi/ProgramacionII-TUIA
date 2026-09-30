# Cuando trabajamos con objetos, podemos escribir funciones de dos maneras
# distintas:
# Una función modificadora cambia el objeto que recibe.
# Una función pura no toca el objeto original: crea y devuelve un objeto
# nuevo con el cambio aplicado.
# Definí una clase Producto con los atributos nombre y precio .
# Ahora, fuera de la clase, escribí dos funciones que apliquen un descuento (un
# porcentaje):
# rebajar(producto, porcentaje) : es una función modificadora. Baja el precio
# del producto que recibe según el porcentaje indicado, cambiando ese mismo
# producto. No devuelve nada.
# con_descuento(producto, porcentaje) : es una función pura. No modifica el
# producto que recibe; en su lugar, crea y devuelve un nuevo Producto con el
# precio ya rebajado.
# Escribí código que muestre la diferencia entre ambas: después de llamar a
# con_descuento , el producto original conserva su precio; después de llamar a
# rebajar , el producto original quedó más barato.

class Producto():

    def __init__(self, nombre: str, precio: float) -> None:
        self.nombre = nombre
        self.precio = precio
    
#Funcion modificadora
def rebajar(prod: Producto, porcentaje: int) -> None:
    descuento = prod.precio * (porcentaje / 100)
    prod.precio = prod.precio - descuento

#funcion pura
def con_descuento(prod: Producto, porcentaje: int) -> Producto:
    descuento = prod.precio * (porcentaje / 100)
    nuevo_precio = prod.precio - descuento

    # no hace falta colocar la variable, puede devolverse en el return el objeto
    productoNuevo = Producto(prod.nombre, nuevo_precio)
    return productoNuevo

#ejemplo funcion modificadora
pantalon = Producto("Pantalon", 3000)
resultado2 = rebajar(pantalon, 25)
print(pantalon.nombre, pantalon.precio)

#ejemplo funcion pura
remera = Producto("Remera", 1500)
resultado1 = con_descuento(remera, 15)
print(resultado1.nombre, resultado1.precio)
print(remera.nombre, remera.precio)
