import problemaPS6

def test_encontrar_mayor():
    assert problemaPS6.encontrar_mayor(1.0, 2.0, 3.0) == 3.0
    assert problemaPS6.encontrar_mayor(3.0, 2.0, 1.0) == 3.0
    assert problemaPS6.encontrar_mayor(2.0, 3.0, 1.0) == 3.0
    assert problemaPS6.encontrar_mayor(1.1, 1.1, 1.1) == 1.1
    assert problemaPS6.encontrar_mayor(-1.0, -2.0, -3.0) == -1.0
    assert problemaPS6.encontrar_mayor(0.0, 0.0, 1.0) == 1.0
    print("Todos los casos de prueba pasaron exitosamente.")