def print_string(n: int, s: str) -> str:

    # caso base
    if n == 0:
        return ""
    # caso recursivo
    return s +"\n" + print_string(n-1, s)

print1 = print_string(3, "Hola")
print(print1)
