import csv
from collections import defaultdict


#Tipo 4: Extracción de clases: Votacion
class Votacion:
    def __init__(self, archivo_datos):
        self.archivo_datos = archivo_datos

    def leer_datos(self):
        datos = []
        with open(self.archivo_datos, 'r') as csvfile:
            next(csvfile)
            datareader = csv.reader(csvfile)
            for fila in datareader:
                datos.append(fila)
        return datos

class CalculaGanador:
    def __init__(self,datos):

        # Tipo 2: Renombrar variables: data a datos - votosxcandidato a votos_por_candidato
        self.datos = datos
        self.votos_por_candidato = defaultdict(int)

# Tipo 1: extracción de métodos (4)
    # es_dni_valido(dni)
    def es_din_valido(self,dni):
        return len(dni) == 8 and dni.isdigit()  #Tipo 3: Simplificación de condicionales

    #contar_votos_validos()
    def contar_votos_validos(self):
        for fila in self.datos:
            candidato = fila[4]
            es_valido = fila[5] == '1'
            dni = fila [3]
            if self.es_din_valido(dni) and es_valido:
                self.votos_por_candidato[candidato] += 1
    #calcular_porcentaje_votos()
    def calcular_porcentaje_votos(self):
        total_votos_validos = sum(self.votos_por_candidato.values())
         
        return {candidato: (votos / total_votos_validos) * 100 for candidato, votos in self.votos_por_candidato.items()}
    
    #Determinar_ganador()
    #Tipo 5: Divisón de métodos - determinar_ganador
    def determinar_ganador(self):
        self.contar_votos_validos()
        porcentaje_votos = self.calcular_porcentaje_votos()
        candidatos_ordenados = sorted(porcentaje_votos.items(), key=lambda item: item[1], reverse=True)

        for candidato, votos in self.votos_por_candidato.items():
            print(f'candidato: {candidato} votos validos: {votos}')
        
        if candidatos_ordenados[0][1] > 50:
            return [candidatos_ordenados[0][0]]
        
        if len(candidatos_ordenados) > 1 and candidatos_ordenados[0][1] == 50:
            return [candidatos_ordenados[0][0]]
        
        return [candidatos_ordenados[0][0], candidatos_ordenados[1][0]] if len(candidatos_ordenados) > 1 else [candidatos_ordenados[0][0]]

def main():
    archivo_datos = '0204.csv'
    votacion = Votacion(archivo_datos)
    datos = votacion.leer_datos()
    calcula_ganador = CalculaGanador(datos)
    resultado = calcula_ganador.determinar_ganador()
    print(resultado)

    # Datos de prueba
    datos_prueba = [
        ['Áncash', 'Asunción', 'Acochaca', '40810062', 'Eddie Hinesley', '0'],
        ['Áncash', 'Asunción', 'Acochaca', '57533597', 'Eddie Hinesley', '1'],
        ['Áncash', 'Asunción', 'Acochaca', '86777322', 'Aundrea Grace', '1'],
        ['Áncash', 'Asunción', 'Acochaca', '23017965', 'Aundrea Grace', '1']
    ]
    calcula_ganador_prueba = CalculaGanador(datos_prueba)
    resultado_prueba = calcula_ganador_prueba.determinar_ganador()
    print(resultado_prueba)

if __name__ == "__main__":
    main()

#Cambios realizados:

#-------------------------------------Extracción de métodos:

#es_dni_valido: Método para validar el DNI.
#contar_votos_validos: Método para contar votos válidos.
#calcular_porcentaje_votos: Método para calcular el porcentaje de votos por candidato.
#determinar_ganador: Método principal para determinar el ganador.

#----------------------------------Renombrar variables:

#data a datos.
#votosxcandidato a votos_por_candidato.

#--------------------------------------Extracción de clases:

#Nueva clase Votacion para manejar la lectura de datos.

#---------------------------------Simplificación de condicionales:

#Validación del DNI simplificada con len(dni) == 8 and dni.isdigit().
#Uso de defaultdict para inicializar los votos.

#-----------------------------------División de métodos:

#Método determinar_ganador que combina los pasos para determinar el ganador de manera más limpia.






        