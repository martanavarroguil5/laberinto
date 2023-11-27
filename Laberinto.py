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
