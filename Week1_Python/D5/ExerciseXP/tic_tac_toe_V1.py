def print_board(board):
    print("*******************")
    print("* {} | {} | {} *".format(board[0][0], board[0][1], board[0][2]))
    print("*---|---|---*")
    print("* {} | {} | {} *".format(board[1][0], board[1][1], board[1][2]))
    print("*---|---|---*")
    print("* {} | {} | {} *".format(board[2][0], board[2][1], board[2][2]))
    print("*******************")

def check_winner(board, player):
    for row in board:
        if all([spot == player for spot in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def check_tie(board):
    return all([spot != " " for row in board for spot in row])

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    while True:
        print_board(board)
        print(f"Player {players[turn % 2]}'s turn...")
        row = int(input("Enter row (0, 1, 2): "))
        col = int(input("Enter column (0, 1, 2): "))

        if board[row][col] != " ":
            print("This spot is already taken! Try again.")
            continue

        board[row][col] = players[turn % 2]
        turn += 1

        if check_winner(board, players[turn % 2 - 1]):
            print_board(board)
            print(f"Player {players[turn % 2 - 1]} wins!")
            break

        if check_tie(board):
            print_board(board)
            print("The game is a tie!")
            break

if __name__ == "__main__":
    main()
