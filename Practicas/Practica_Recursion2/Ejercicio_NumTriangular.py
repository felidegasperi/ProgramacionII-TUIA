def numTriangular(n: int) -> int:
    # casos base
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # caso recursivo
    else:
        return numTriangular(n - 1) + n

enesimo = numTriangular(6)

print(enesimo)