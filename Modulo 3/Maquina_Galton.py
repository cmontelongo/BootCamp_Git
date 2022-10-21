import random
import matplotlib.pyplot as plt

def llenar_arreglo(total_canicas, obstaculos):
    '''
    Función donde se realizan 2 ciclos para obtener las posiciones finales de las canicas
    dentro del arreglo de obtáculos.

    Se considera movimiento izquierdo y derecho dentro del arreglo y de manera aleatorea
    según el total de obstáculos será la posición final después del ciclo.

    Al final se obtiene un arreglo donde se almacena un total de canicas por obstáculo
    ó posición.
    '''
    # Arreglo para almacenar el total de canicas por obstáculo
    arreglo_maquina = [0]*(obstaculos)

    # Ciclo principal donde se toma el total de canicas
    for i in range(total_canicas):
        # Inicia en 0 y se incrementará para terminar la posición en el arreglo
        canica_posicion_maquina = 0
        # Ciclo para generar un valor de 0 ó 1.
        # Conserando 0 como izquierda y 1 como derecha dentro del arreglo final
        for j in range(obstaculos):
            # Valor aleatorio de 0 ó 1
            canica_posicion_maquina += random.randint(0, 1)
        # Asegurarse que la posición final no esté dentro de los límites del número de obstáculos
        if canica_posicion_maquina >= obstaculos:
            # Se alcanzó el límite y se asigna la última posición dentro del arreglo
            canica_posicion_maquina = obstaculos-1
        # Posicion final despues del recorrido aleatorio entre el numero de obstáculos
        arreglo_maquina[canica_posicion_maquina] += 1

    # Regresar el arreglo final con la canicas posicionadas después de los ciclos
    return arreglo_maquina


def mostrar_grafico(arreglo):
    '''
    Función para generar un gráfico de barras de acuerdo a un arreglo recibido como parámetro.

    Se mostrarán título, valores de X e Y.
    '''
    plt.title('Simulación de la Máquina de Galton')
    plt.ylabel('Numero de canicas')
    plt.xlabel('Distribución de canicas')
    # Generar gráfico de barras, se indica ancho de la barra en lo más ancho y de color verde
    plt.bar(range(len(arreglo)), arreglo, width=1, color='green')
    # Mostrar el gráfico en pantalla
    plt.show()


##########################################################################
# Iniciar las variables globales para controlar la generación del gráfico
# Número total de canicas
numero_canicas = 3000
# Total de obstaculos en el arreglo final
niveles_obstaculos = 12

# Invocar funcion para llegar arreglo de la Máquina Galton
maquina_grafico = llenar_arreglo(numero_canicas, niveles_obstaculos)

# Mostrar los valores generados
print(maquina_grafico)

# Generar gráfico con el arreglo obtenido previamente
mostrar_grafico(maquina_grafico)

print('-'*30)
print('-----> FIN DEL PROGRAMA <-----')
print('-'*30)
