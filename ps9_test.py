import ps9

def test_convertir_unidad():
    assert ps9.convertir_unidad(1, 1, 1) == 25.40
    assert ps9.convertir_unidad(1, 2, 1) == 0.9144
    assert ps9.convertir_unidad(2, 1, 1) == 0.02832
    assert ps9.convertir_unidad(3, 1, 1) == 28.35
    assert ps9.convertir_unidad(4, 1, 1) is None

    print("Todos los casos de prueba pasaron exitosamente.")