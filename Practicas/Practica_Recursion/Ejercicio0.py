#  Escriba una función recursiva factorial que tome un numero natural n y calcule su factorial n!.
def factorial(num: int) -> int:
    if num == 0:
        return 1
    return num * factorial(num - 1)