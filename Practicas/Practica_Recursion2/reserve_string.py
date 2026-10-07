# definición recursiva
def reverse_string_rec(string: str) -> str:
    # caso base
    if len(string) == 0:
        return ""
    # caso recursivo
    return reverse_string_rec(string[1:]) + string[0]

ej_rec = reverse_string_rec("Hola")

print(ej_rec)

# definicion iterativa
def reverse_string_ite(string: str) -> str:
    resultado = ""
    for i in string:
        resultado = i + resultado

    return resultado

ej_ite = reverse_string_ite("Hola")

print(ej_ite)