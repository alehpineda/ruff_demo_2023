from typing import Iterable


def sumar_numeros_pares(numeros: Iterable[int]) -> int:
    return sum(num for num in numeros if num % 2 == 0)


def sumar_numeros_impares(numeros: Iterable[int]) -> int:
    return sum(num for num in numeros if num % 2 == 1)
