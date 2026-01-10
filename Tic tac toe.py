def print_board(b):
    for row in b:
        print(" | ".join(row))
        print("-" * 9)

def check_win(b, p):
    for i in range(3):
        if all(b[i][j] == p for j in range(3)) or all(b[j][i] == p for j in range(3)):
            return True
    if all(b[i][i] == p for i in range(3)) or all(b[i][2-i] == p for i in range(3)):
        return True
    return False

def play():
    board = [[" " for _ in range(3)] for _ in range(3)]
    turn = "X"
    for _ in range(9):
        print_board(board)
        try:
            row, col = map(int, input(f"Player {turn} (row col 0-2): ").split())
            if board[row][col] != " ":
                print("Taken!")
                continue
            board[row][col] = turn
            if check_win(board, turn):
                print_board(board)
                print(f"Player {turn} wins!")
                return
            turn = "O" if turn == "X" else "X"
        except:
            print("Invalid input.")
    print_board(board)
    print("Draw!")

play()

# TYPE THE NUMBER OF THE ROW AND COLUMN