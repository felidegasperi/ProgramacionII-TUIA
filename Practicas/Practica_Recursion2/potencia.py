def power(a: int, b:int) -> int:

    # casos base para a y b
    if a == 0:
        return 0
    elif b == 0:
        return 1
    # caso recursivo con b par
    elif b % 2 == 0:
        p = power(a, b // 2)
        return p * p
    # caso recursivo b impar
    else:
        p = power(a, (b - 1) // 2)
        return p * p * a

potencia = power(3,2)

print(potencia)