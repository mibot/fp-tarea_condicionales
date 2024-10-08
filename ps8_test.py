import ps8

def test_convertir_unidad():
    assert ps8.convertir_unidad(1, 1) == 25.40
    assert ps8.convertir_unidad(2, 1) == 0.9144
    assert ps8.convertir_unidad(3, 1) == 1.6093
    assert ps8.convertir_unidad(1, 2) == 50.80
    assert ps8.convertir_unidad(2, 2) == 1.8288
    assert ps8.convertir_unidad(3, 2) == 3.2186
    assert ps8.convertir_unidad(4, 1) is None
    print("Todos los casos de prueba pasaron exitosamente.")