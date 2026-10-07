def fibonacci(n: int) -> int:

    # caso base
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n -1) + fibonacci(n - 2)

fibo = fibonacci(7)
print(fibo)