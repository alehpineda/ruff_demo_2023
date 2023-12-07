def sumar_numeros_pares(numeros):
    return sum(num for num in numeros if num % 2 == 0)


def sumar_numeros_impares(numeros):
    return sum(num for num in numeros if num % 2 == 1)
