# pasar esta funcion iterativa a recursiva
def iterativa(l: list[int])-> int:
    c = 1
    for i in l:
        c = c * i
    return c   

# ---------------

def recursiva(l: list[int]) -> int:
    c = 1
    if (len(l)) == 0:
        return 1
    else:
        return l[0] * recursiva(l[1:])

recur = recursiva([1,3,2])

print(recur)