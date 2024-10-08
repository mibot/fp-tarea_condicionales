import ps12


def test_todos_digitos_pares():
    assert ps12.todos_digitos_pares(2468) == True
    assert ps12.todos_digitos_pares(1234) == False
    assert ps12.todos_digitos_pares(6244) == True
    assert ps12.todos_digitos_pares(5688) == False
    assert ps12.todos_digitos_pares(999) == False  # Menos de 4 dígitos
    assert ps12.todos_digitos_pares(10000) == False  # Más de 4 dígitos
    print("Todas las pruebas pasaron exitosamente.")