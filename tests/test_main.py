from src.main import sumar_numeros_impares, sumar_numeros_pares


def test_sumar_numeros_pares() -> None:
    assert sumar_numeros_pares([1, 2, 3, 4, 5, 6]) == 12
    # no hay pares
    assert sumar_numeros_pares([1, 3, 5]) == 0
    # no hay numeros
    assert sumar_numeros_pares([]) == 0


def test_sumar_numeros_impares() -> None:
    assert sumar_numeros_impares([1, 2, 3, 4, 5, 6]) == 9
    # no hay pares
    assert sumar_numeros_impares([2, 4, 6]) == 0
    # no hay numeros
    assert sumar_numeros_impares([]) == 0
