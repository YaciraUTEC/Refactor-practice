# Refactor-practice
## Integrantes
- Yacira Nicol Campoverde San Martín

### Cambios realizados:

***Extracción de métodos:***

- es_dni_valido: Método para validar el DNI.
- contar_votos_validos: Método para contar votos válidos.
- calcular_porcentaje_votos: Método para calcular el porcentaje de votos por candidato.
- determinar_ganador: Método principal para determinar el ganador.

***Renombrar variables:***

- data a datos.
- votosxcandidato a votos_por_candidato.

***Extracción de clases:***

- Nueva clase Votacion para manejar la lectura de datos.

***Simplificación de condicionales:***

- Validación del DNI simplificada con len(dni) == 8 and dni.isdigit().
- Uso de defaultdict para inicializar los votos.

***División de métodos:***

- Método determinar_ganador que combina los pasos para determinar el ganador de manera más limpia.




