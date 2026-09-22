# Escriba una función recursiva repite_hola que reciba como parámetro un número entero n y
# escriba por pantalla n veces el mensaje "Hola". Invóquela con distintos valores de n

def repite_hola(num: int, st: str) -> str:
    if num == 0:
        print()
    else:
        print(
            num * repite_hola(num, st)
        )
        
    