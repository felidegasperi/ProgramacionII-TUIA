def find_max(l: list[int]) -> int:

    # caso base
    if len(l) == 0:
        return 0

    #caso recursivo
    return max(l)

lista_max = find_max([])

print(lista_max)