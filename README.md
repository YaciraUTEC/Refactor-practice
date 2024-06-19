# Refactor-practice
## Integrantes
- Yacira Nicol Campoverde San Martín
- Sebastian Rejas Berrios

### TIPOS DE EXTRACCIONES 

1. ***Extracción de métodos:***

- es_dni_valido: Método para validar el DNI.
- contar_votos_validos: Método para contar votos válidos.
- calcular_porcentaje_votos: Método para calcular el porcentaje de votos por candidato.
- determinar_ganador: Método principal para determinar el ganador.

2. ***Renombrar variables:***

- data a datos.
- votosxcandidato a votos_por_candidato.

3. ***Extracción de clases:***

- Nueva clase Votacion para manejar la lectura de datos.

4. ***Simplificación de condicionales:***

- Validación del DNI simplificada con len(dni) == 8 and dni.isdigit().
- Uso de defaultdict para inicializar los votos.

5. ***División de métodos:***

- Método determinar_ganador que combina los pasos para determinar el ganador de manera más limpia.

-----------------------------------------------------------------------
### EVALUACIÓN DEL CODIGO RESULTANTE
**Uso de Clases y Métodos**

Se han utilizado *clases* (Votacion y CalculaGanador) para organizar la lógica relacionada con la votación y el cálculo del ganador. Esto facilita la reutilización del código y lo hace más modular.
Métodos Bien Definidos:

Los *métodos*:
es_din_valido, contar_votos_validos, calcular_porcentaje_votos y determinar_ganador están bien definidos y separan claramente las responsabilidades dentro de la clase CalculaGanador. Esto mejora la legibilidad y la mantenibilidad del código.

**Manejo de Archivos CSV:**

El método leer_datos en la clase Votacion maneja la lectura de datos desde un archivo CSV, omitiendo la primera línea (probablemente el encabezado), lo cual es un buen enfoque para evitar procesar datos no deseados.  

**Uso de defaultdict:**

El uso de defaultdict(int) para self.votos_por_candidato en CalculaGanador es apropiado, ya que simplifica el conteo de votos por candidato al manejar automáticamente las claves que no existen.


