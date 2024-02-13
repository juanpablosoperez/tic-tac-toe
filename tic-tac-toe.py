# definir estructura del tablero
tablero = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]


#  dibujar el tablero
def mostrar_tablero(tablero):
    print(" ")
    for i in range(3):
        print('|'.join(tablero[i]))
        if i < 2:
            print("-----")
    print(" ")


# verificar ganador
def verificar_ganador(tablero):
    # Verificar filas
    for fila in tablero:
        if fila[0] == fila[1] == fila[2] != ' ':
            return fila[0]

    # Verificar columnas
    for col in range(3):
        if tablero[0][col] == tablero[1][col] == tablero[2][col] != ' ':
            return tablero[0][col]

    # Verificar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != ' ':
        return tablero[0][0]
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != ' ':
        return tablero[0][2]

    return None


# funcion principal
def jugar_tic_tac_toe():
    jugador_actual = 'X'
    jugadas_restantes = 9
    ganador = None

    # bucle principal
    while jugadas_restantes > 0 and not ganador:
        mostrar_tablero(tablero)
        print("Turno del jugador", jugador_actual)
        fila = int(input("Ingresa el número de fila (0, 1 o 2): "))
        columna = int(input("Ingresa el número de columna (0, 1 o 2): "))

        if tablero[fila][columna] == ' ':
            tablero[fila][columna] = jugador_actual
            jugadas_restantes -= 1
            ganador = verificar_ganador(tablero)
            jugador_actual = 'O' if jugador_actual == 'X' else 'X'
        else:
            print("¡Posición inválida! Inténtalo de nuevo.")

    mostrar_tablero(tablero)

    if ganador:
        print("¡El jugador", ganador, "ha ganado!")
    else:
        print("¡Es un empate!")


jugar_tic_tac_toe()



