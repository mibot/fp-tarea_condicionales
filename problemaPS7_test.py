import math
import problemaPS7

def test_calcular_fx():
    assert problemaPS7.calcular_fx(4) == 64
    assert problemaPS7.calcular_fx(5) == -0.056
    assert problemaPS7.calcular_fx(6) == 221
    assert problemaPS7.calcular_fx(7) == math.sqrt(7)
    assert problemaPS7.calcular_fx(8) == 512
    print("Todos los casos de prueba pasaron exitosamente.")
