import problemaPS3

def test_es_divisor():
    assert problemaPS3.es_divisor(3, 9) == True
    assert problemaPS3.es_divisor(4, 9) == False
    assert problemaPS3.es_divisor(5, 25) == True
    assert problemaPS3.es_divisor(7, 22) == False
    assert problemaPS3.es_divisor(0, 5) == False
    assert problemaPS3.es_divisor(5, 0) == True  # Todo número (excepto 0) es divisor de 0
    print("Todos los casos de prueba pasaron exitosamente.")