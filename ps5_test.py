import ps5

def test_calcular_precio_con_descuento():
    assert ps5.calcular_precio_con_descuento(500) == 500.0
    assert ps5.calcular_precio_con_descuento(1000) == 900.0
    assert ps5.calcular_precio_con_descuento(3000) == 2550.0
    assert ps5.calcular_precio_con_descuento(6000) == 4800.0
    print("Todos los casos de prueba pasaron exitosamente.")