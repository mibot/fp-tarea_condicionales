import problemaPS4

def test_estan_en_orden_creciente():
    assert problemaPS4.estan_en_orden_creciente(1, 2, 3) == True
    assert problemaPS4.estan_en_orden_creciente(1, 3, 2) == False
    assert problemaPS4.estan_en_orden_creciente(3, 2, 1) == False
    assert problemaPS4.estan_en_orden_creciente(-3, 0, 5) == True
    print("Todos los casos de prueba pasaron exitosamente.")