import random

def display_board(board):
    for row in board:
        print("+-------+-------+-------+")
        print("|   {}   |   {}   |   {}   |".format(row[0], row[1], row[2]))
    print("+-------+-------+-------+")

def enter_move(board):
    while True:
        move = input("Ingresa tu movimiento (1-9): ")
        if move.isdigit() and 1 <= int(move) <= 9:
            row = (int(move) - 1) // 3
            col = (int(move) - 1) % 3
            if isinstance(board[row][col], int):
                board[row][col] = 'O'
                return
        print("Movimiento inválido. Intenta de nuevo.")

def make_list_of_free_fields(board):
    return [(row, col) for row in range(3) for col in range(3) if isinstance(board[row][col], int)]

def victory_for(board, sign):
    for i in range(3):
        if all(board[i][j] == sign for j in range(3)) or all(board[j][i] == sign for j in range(3)):
            return True
    if all(board[i][i] == sign for i in range(3)) or all(board[i][2-i] == sign for i in range(3)):
        return True
    return False

def draw_move(board):
    free_fields = make_list_of_free_fields(board)
    if free_fields:
        row, col = random.choice(free_fields)
        board[row][col] = 'X'

def play_game():
    board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    board[1][1] = 'X'  # La máquina siempre empieza en el centro
    
    while True:
        display_board(board)
        
        if victory_for(board, 'X'):
            print("¡La máquina gana!")
            break
        elif not make_list_of_free_fields(board):
            print("¡Empate!")
            break
        
        enter_move(board)
        
        if victory_for(board, 'O'):
            display_board(board)
            print("¡Has ganado!")
            break
        elif not make_list_of_free_fields(board):
            display_board(board)
            print("¡Empate!")
            break
        
        draw_move(board)

if __name__ == "__main__":
    play_game()