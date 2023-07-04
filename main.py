import random

def print_board(board):
    print("-------------")
    print("|", board[0], "|", board[1], "|", board[2], "|")
    print("-------------")
    print("|", board[3], "|", board[4], "|", board[5], "|")
    print("-------------")
    print("|", board[6], "|", board[7], "|", board[8], "|")
    print("-------------")

def is_winner(board, player):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] == player:
            return True

    # Check columns
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] == player:
            return True

    # Check diagonals
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True

    return False

def is_board_full(board):
    return all(cell != " " for cell in board)

def get_computer_move(board):
    # Check for winning moves
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            if is_winner(board, "O"):
                return i
            else:
                board[i] = " "

    # Check for player winning moves
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            if is_winner(board, "X"):
                board[i] = "O"
                return i
            else:
                board[i] = " "

    # Choose a random move
    available_moves = [i for i, cell in enumerate(board) if cell == " "]
    return random.choice(available_moves)

def play_game():
    board = [" "]*9
    print("Tic Tac Toe - You are X and the computer is O")
    print_board(board)

    while True:
        # Player's move
        player_move = input("Enter a number (1-9) to make your move: ")
        player_move = int(player_move) - 1

        if board[player_move] != " ":
            print("Invalid move. Try again.")
            continue

        board[player_move] = "X"
        print_board(board)

        if is_winner(board, "X"):
            print("Congratulations! You won!")
            break

        if is_board_full(board):
            print("It's a tie!")
            break

        # Computer's move
        print("Computer's turn...")
        computer_move = get_computer_move(board)
        board[computer_move] = "O"
        print_board(board)

        if is_winner(board, "O"):
            print("Sorry! You lost!")
            break

        if is_board_full(board):
            print("It's a tie!")
            break

play_game()
