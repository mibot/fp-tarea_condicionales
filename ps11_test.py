import ps11
import math

def test_problema_11():
    # Prueba es_triangulo
    assert ps11.es_triangulo(3, 4, 5) == True
    assert ps11.es_triangulo(1, 1, 3) == False

    # Prueba calcular_area
    assert math.isclose(ps11.calcular_area(3, 4, 5), 6.0, rel_tol=1e-9)

    # Prueba determinar_tipo_triangulo
    assert ps11.determinar_tipo_triangulo(3, 3, 3) == "equilátero"
    assert ps11.determinar_tipo_triangulo(3, 3, 4) == "isósceles"
    assert ps11.determinar_tipo_triangulo(3, 4, 5) == "escaleno"

    print("Todas las pruebas pasaron exitosamente.")