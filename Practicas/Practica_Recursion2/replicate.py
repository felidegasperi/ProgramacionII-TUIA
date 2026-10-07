def replicate(l: list[int], num: int) -> list:
    # caso base
    if len(l) == 0 or num == 0:
        return []
    else:
    # caso recursivo
        return [l[0]] * num + replicate(l[1:], num)

prueba = replicate([1, 5, 4], 2)

print(prueba)