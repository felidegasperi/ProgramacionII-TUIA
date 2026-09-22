def factorial(n: int) -> int:

    # caso base
    if n == 0:
        return 1

    if n < 0:
        return 0
    
    #caso recursivo
    return n * factorial(n - 1)


ej = factorial(5)

print(ej)