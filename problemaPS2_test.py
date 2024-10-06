import problemaPS2

def test_calcular_nuevo_salario():
    assert problemaPS2.calcular_nuevo_salario(15000) == 16800.0
    assert problemaPS2.calcular_nuevo_salario(20000) == 21600.0
    assert problemaPS2.calcular_nuevo_salario(40000) == 42800.0
    assert problemaPS2.calcular_nuevo_salario(60000) == 63600.0
    print("Todos los casos de prueba pasaron exitosamente.")