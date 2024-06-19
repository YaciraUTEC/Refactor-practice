import unittest
from io import StringIO
from unittest.mock import patch
from collections import defaultdict

# Aquí importamos las clases y funciones que queremos probar
from apprefactor import Votacion, CalculaGanador

class TestVotacion(unittest.TestCase):
    def setUp(self):
        # Configuración inicial para las pruebas si es necesaria
        self.datos_prueba = [
            ['Áncash', 'Asunción', 'Acochaca', '40810062', 'Eddie Hinesley', '0'],
            ['Áncash', 'Asunción', 'Acochaca', '57533597', 'Eddie Hinesley', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '86777322', 'Aundrea Grace', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '23017965', 'Aundrea Grace', '1']
        ]

    def test_leer_datos(self):
        votacion = Votacion('0204.csv')
        datos = votacion.leer_datos()
        self.assertEqual(len(datos), 4)  # Verificamos que se lean 4 filas como en el ejemplo

    def test_es_din_valido(self):
        calcula_ganador = CalculaGanador([])
        self.assertTrue(calcula_ganador.es_din_valido('40810062'))  # DNI válido
        self.assertFalse(calcula_ganador.es_din_valido('1234567'))  # DNI inválido

    def test_contar_votos_validos(self):
        calcula_ganador = CalculaGanador(self.datos_prueba)
        calcula_ganador.contar_votos_validos()
        self.assertEqual(calcula_ganador.votos_por_candidato['Eddie Hinesley'], 1)
        self.assertEqual(calcula_ganador.votos_por_candidato['Aundrea Grace'], 2)

    def test_calcular_porcentaje_votos(self):
        calcula_ganador = CalculaGanador(self.datos_prueba)
        calcula_ganador.contar_votos_validos()
        porcentaje_votos = calcula_ganador.calcular_porcentaje_votos()
        self.assertAlmostEqual(porcentaje_votos['Eddie Hinesley'], 25.0, delta=0.1)  # Aproximadamente 25%
        self.assertAlmostEqual(porcentaje_votos['Aundrea Grace'], 50.0, delta=0.1)  # Aproximadamente 50%

    def test_determinar_ganador(self):
        calcula_ganador = CalculaGanador(self.datos_prueba)
        resultado = calcula_ganador.determinar_ganador()
        self.assertIn('Aundrea Grace', resultado)  # Verificar que Aundrea Grace está en los resultados esperados

    # Este método prueba la salida estándar
    @patch('sys.stdout', new_callable=StringIO)
    def test_determinar_ganador_output(self, mock_stdout):
        calcula_ganador = CalculaGanador(self.datos_prueba)
        calcula_ganador.determinar_ganador()
        output = mock_stdout.getvalue().strip()
        self.assertIn('candidato: Eddie Hinesley votos validos: 1', output)
        self.assertIn('candidato: Aundrea Grace votos validos: 2', output)

if __name__ == '__main__':
    unittest.main()

