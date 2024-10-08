import math
import ps7

def test_calcular_fx():
    assert ps7.calcular_fx(4) == 64
    assert ps7.calcular_fx(5) == -0.056
    assert ps7.calcular_fx(6) == 221
    assert ps7.calcular_fx(7) == math.sqrt(7)
    assert ps7.calcular_fx(8) == 512
    print("Todos los casos de prueba pasaron exitosamente.")
