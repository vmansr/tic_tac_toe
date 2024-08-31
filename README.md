# Tic-Tac-Toe Simplificado en Python

## Descripción

Este proyecto implementa una versión simplificada del juego Tic-Tac-Toe (también conocido como Tres en Raya) en Python. El juego se juega entre un usuario humano y la computadora.

## Características

- La máquina juega con 'X' y el usuario con 'O'.
- El primer movimiento siempre lo hace la máquina, colocando una 'X' en el centro del tablero.
- Los cuadros están numerados del 1 al 9.
- El usuario ingresa su movimiento introduciendo el número del cuadro elegido.
- El programa verifica si el juego ha terminado después de cada movimiento.
- La máquina elige sus movimientos de manera aleatoria.

## Cómo jugar

1. Ejecute el script `tic_tac_toe.py`.
2. El juego comenzará con la máquina haciendo el primer movimiento.
3. Cuando sea su turno, ingrese un número del 1 al 9 para hacer su movimiento.
4. El juego continuará hasta que haya un ganador o un empate.

## Reglas

- Los números del 1 al 9 representan las posiciones en el tablero:

  ```
  1 | 2 | 3
  ---------
  4 | 5 | 6
  ---------
  7 | 8 | 9
  ```

- No se puede elegir una posición que ya esté ocupada.
- El juego termina cuando un jugador tiene tres de sus símbolos en línea (horizontal, vertical o diagonal) o cuando todas las casillas están llenas (empate).

## Requisitos

- Python 3.x

## Cómo ejecutar

```bash
python tic_tac_toe.py
```

## Estructura del código

El código está organizado en varias funciones:

- `display_board(board)`: Muestra el estado actual del tablero.
- `enter_move(board)`: Maneja el movimiento del usuario.
- `make_list_of_free_fields(board)`: Crea una lista de las casillas libres.
- `victory_for(board, sign)`: Verifica si hay un ganador.
- `draw_move(board)`: Realiza el movimiento de la máquina.
- `play_game()`: Controla el flujo principal del juego.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abra un issue primero para discutir qué le gustaría cambiar.
