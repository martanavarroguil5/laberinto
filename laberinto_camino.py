'''
con una tupla indico qué casillas tienen muros'''
muro = ((0, 1), (0, 2), (0, 3), (0, 4), (1, 1), (2, 1), (2, 3), (3, 3), (4, 0), (4, 1), (4, 2), (4, 3))

'''
indico las dimensiones del laberinto. cada fila es una lista llena de espacios.'''
filas = 5
columnas = 5

'''
creo el laberinto inicialmente lleno de espacios'''
laberinto = [[' ' for _ in range(columnas)] for _ in range(filas)]

'''
pongo muros en el laberinto'''
for coord in muro:
    fila, col = coord
    laberinto[fila][col] = 'X'

# print
for fila in laberinto:
    print(' '.join(fila))

'''
defino una función llamada encontrar_camino que toma tres argumentos: el laberinto y las coordenadas de inicio y fin'''
def encontrar_camino(laberinto, inicio, fin):
    '''
    defino una funcion intetrna que toma la posición actual en el laberinto y la secuencia de movimientos hasta ese punto'''
    def buscar(posicion_actual, camino_actual):
        '''
        Verificamos si la posición actual es igual a la posición de destino (fin). Si es así, añadimos la secuencia actual de 
        movimientos a la lista caminos_posibles'''
        if posicion_actual == fin:
            caminos_posibles.append(list(camino_actual))
            return
        x, y = posicion_actual

        '''
        vemos cuales son las direcciones posibles (arriba, abajo, izquierda, derecha) a partir de la posición actual.'''
        for direccion in direcciones:
            nueva_x, nueva_y = x + direccion[0], y + direccion[1]

            '''
            hacemos que no sea posible salirse de los límites del laberinto o de los muros'''
            if (
                0 <= nueva_x < filas
                and 0 <= nueva_y < columnas
                and laberinto[nueva_x][nueva_y] != 'X'
                and (nueva_x, nueva_y) not in visitados
            ):
                '''
                Si el movimiento es válido, marcamos la nueva posición como visitada, añadimos el movimiento actual a la
                secuencia y continuamos la búsqueda desde la nueva posición'''
                visitados.add((nueva_x, nueva_y))
                camino_actual.append(direccion_str[direccion])
                buscar((nueva_x, nueva_y), camino_actual)
                visitados.remove((nueva_x, nueva_y))
                camino_actual.pop()

    '''
    Definimos las direcciones posibles y un diccionario para traducir las direcciones como arriba, abajo, derecha, izquierda'''
    direcciones = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    direccion_str = {(-1, 0): 'Arriba', (1, 0): 'Abajo', (0, 1): 'Derecha', (0, -1): 'Izquierda'}

    filas = len(laberinto)
    columnas = len(laberinto[0])

    '''
    Creamos la lista de visitados y la de caminos_posibles que registra las direcciones que hay que tomar para finalizar el 
    laberinto. Marcamos la posición de inicio como visitada y comenzamos la búsqueda desde esa posición'''
    visitados = set()
    caminos_posibles = []
    buscar(inicio, [])
    # Devuelve el primer camino encontrado o None si no hay caminos
    return caminos_posibles[0] if caminos_posibles else None

# Coordenadas de inicio y fin
inicio = (0, 0)
fin = (filas - 1, columnas - 1)

# Buscar el camino
camino = encontrar_camino(laberinto, inicio, fin)

# Imprimir el resultado
print(camino)
