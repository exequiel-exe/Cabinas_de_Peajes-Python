import random
import matplotlib.pyplot as plt
from TDA_COLA.TDA_COLA import *

#Los gráficos se muestran en ventanas individuales. Es necesario cerrar cada ventana para que se genere un nuevo gráfico.

# Definimos las tarifas de los vehículos
tarifas = {
    "automovil": 47,
    "camioneta": 59,
    "camion": 71,
    "colectivo": 64
}

# Mostramos las tarifas en consola
print("Tarifas de los vehículos:")
for vehiculo, tarifa in tarifas.items():
    print(f"- {vehiculo.capitalize()}: ${tarifa}")

# Función para generar vehículos aleatorios
def generar_vehiculo_aleatorio():
    tipos_vehiculos = ["automovil", "camioneta", "camion", "colectivo"]
    return random.choice(tipos_vehiculos)

# Inicializamos las colas para las 3 cabinas
cabina1 = Cola()
cabina2 = Cola()
cabina3 = Cola()

# Agregamos 300 vehículos de manera aleatoria a las cabinas de cobro
for _ in range(300):
    vehiculo = generar_vehiculo_aleatorio()
    random.choice([cabina1, cabina2, cabina3]).agregar(vehiculo)

# Función para procesar las cabinas y calcular los resultados
def procesar_cabinas(cabinas):
    recaudacion = [0] * len(cabinas)
    conteo_vehiculos = [{ "automovil": 0, "camioneta": 0, "camion": 0, "colectivo": 0 } for _ in cabinas]

    # Procesar cada cabina
    for i, cabina in enumerate(cabinas):
        while not cabina.cola_vacia():
            vehiculo = cabina.apartar_actualizar()
            recaudacion[i] += tarifas[vehiculo]
            conteo_vehiculos[i][vehiculo] += 1

    return recaudacion, conteo_vehiculos

# Procesamos las cabinas
recaudacion, conteo_vehiculos = procesar_cabinas([cabina1, cabina2, cabina3])

# Imprimir resultados
print("Número de vehículos atendidos en cada cabina:")
for i, conteo in enumerate(conteo_vehiculos):
    print(f"Cabina {i+1}: {conteo}")

print("Recaudación total en cada cabina:")
for i, total in enumerate(recaudacion):
    print(f"Cabina {i+1}: ${total}")

# Crear grafico de barra individuales para cada cabina
cabinas = ['Cabina 1', 'Cabina 2', 'Cabina 3']

# Gráfico de vehículos atendidos por tipo para cada cabina
for i in range(len(cabinas)):
    # Datos para el grafico de vehículos atendidos
    tipos_vehiculos = list(conteo_vehiculos[i].keys())
    cantidades = list(conteo_vehiculos[i].values())

    # Crear figura para el grafico de barra
    plt.figure(figsize=(10, 5))

    # Grafico de vehículos atendidos
    plt.bar(tipos_vehiculos, cantidades, color='b', alpha=0.7)
    plt.title(f'Vehículos Atendidos - {cabinas[i]}')
    plt.xlabel('Tipo de Vehículo')
    plt.ylabel('Cantidad de Vehículos')
    plt.xticks(rotation=45)

    # Ajustar el layout y mostrar el gráfico
    plt.tight_layout()
    plt.show()

# Crear un gráfico de barras para la recaudación total de cada cabina
plt.figure(figsize=(8, 5))
plt.bar(cabinas, recaudacion, color='orange', alpha=0.7)
plt.title('Recaudación Total por Cabina')
plt.xlabel('Cabinas')
plt.ylabel('Recaudación ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()