def count_digits(number: int) -> int:
    # caso base
    if number < 10:
        return 1
    # caso recursivo
    else:
        return 1 + count_digits(number // 10)

num = count_digits(12435)

print(num)