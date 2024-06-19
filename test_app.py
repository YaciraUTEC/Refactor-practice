import unittest
import csv
from collections import defaultdict
from app import CalculaGanador  # Importa la clase CalculaGanador desde el archivo calcula_ganador.py

class TestCalculaGanador(unittest.TestCase):

    def setUp(self):
        # Datos de prueba comunes para todos los casos
        self.datos_prueba = [
            ['Áncash', 'Asunción', 'Acochaca', '40810062', 'Eddie Hinesley', '0'],
            ['Áncash', 'Asunción', 'Acochaca', '57533597', 'Eddie Hinesley', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '86777322', 'Aundrea Grace', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '23017965', 'Aundrea Grace', '1']
        ]

    def test_un_candidato_ganador(self):
        """
        Caso de prueba para verificar que se identifica correctamente un candidato ganador con más del 50% de votos válidos.
        """
        c = CalculaGanador()
        resultado = c.calcularganador(self.datos_prueba)
        self.assertEqual(resultado, ['Aundrea Grace'])

    def test_empate_exacto(self):
        """
        Caso de prueba para verificar que se maneja correctamente un empate exacto entre dos candidatos con 50% de votos válidos.
        """
        datos_empate = [
            ['Áncash', 'Asunción', 'Acochaca', '40810062', 'Eddie Hinesley', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '57533597', 'Eddie Hinesley', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '86777322', 'Aundrea Grace', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '23017965', 'Aundrea Grace', '1']
        ]
        c = CalculaGanador()
        resultado = c.calcularganador(datos_empate)
        self.assertEqual(resultado, ['Eddie Hinesley'])

    def test_sin_ganador_claro(self):
        """
        Caso de prueba para verificar que se identifican correctamente los dos candidatos que pasan a segunda vuelta cuando no hay un ganador claro.
        """
        datos_sin_ganador = [
            ['Áncash', 'Asunción', 'Acochaca', '40810062', 'Eddie Hinesley', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '57533597', 'Eddie Hinesley', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '86777322', 'Aundrea Grace', '0'],
            ['Áncash', 'Asunción', 'Acochaca', '23017965', 'Aundrea Grace', '0']
        ]
        c = CalculaGanador()
        resultado = c.calcularganador(datos_sin_ganador)
        self.assertEqual(resultado, ['Eddie Hinesley', 'Aundrea Grace'])

    def test_leer_datos(self):
        """
        Caso de prueba para verificar que la función leerdatos() lee el número correcto de filas del archivo de datos.
        """
        c = CalculaGanador()
        datos_leidos = c.leerdatos('test_datos.csv')
        self.assertEqual(len(datos_leidos), 4)  # Verifica que se lean 4 filas como se espera

    def test_es_dni_valido(self):
        """
        Caso de prueba para verificar el método es_dni_valido() con diferentes DNIs válidos e inválidos.
        """
        c = CalculaGanador()
        self.assertTrue(c.es_dni_valido('40810062'))    # DNI válido
        self.assertFalse(c.es_dni_valido('1234567'))    # DNI con longitud incorrecta
        self.assertFalse(c.es_dni_valido('abcdefgh'))   # DNI no numérico

if __name__ == '__main__':
    unittest.main()

