from src.main import sumar_numeros_impares, sumar_numeros_pares


def test_sumar_numeros_pares() -> None:
    assert sumar_numeros_pares([1, 2, 3, 4, 5, 6]) == 12


def test_sumar_numeros_impares() -> None:
    assert sumar_numeros_impares([1, 2, 3, 4, 5, 6]) == 9
