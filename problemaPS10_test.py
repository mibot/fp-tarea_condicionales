import problemaPS10

def test_calcular_pago_total():
    assert problemaPS10.calcular_pago_total(1000, 1, 10) == 1400
    assert problemaPS10.calcular_pago_total(2000, 2, 20) == 3000
    assert problemaPS10.calcular_pago_total(3000, 3, 35) == 5550
    assert problemaPS10.calcular_pago_total(4000, 4, 10) == 4000
    print("Pruebas de cálculo de pago total pasadas con éxito.")