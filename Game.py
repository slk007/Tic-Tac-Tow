import random

# displaying the board
def display_board(board):
    # printing
    print(board[7] + " | " + board[8] + " | " + board[9])
    print("---------")
    print(board[4] + " | " + board[5] + " | " + board[6])
    print("---------")
    print(board[1] + " | " + board[2] + " | " + board[3]+"\n")


# setting up the player
def player_input():
    player1 = input("Please pick a marker O or X: ")
    player2 = "X" if player1 is "O" else "O"

    return (player1, player2)

def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, marker):
    if board[1] == board[2] == board[3] == marker:
        return True
    elif board[4] == board[5] == board[6] == marker:
        return True
    elif board[7] == board[8] == board[9] == marker:
        return True
    elif board[1] == board[4] == board[7] == marker:
        return True
    elif board[2] == board[5] == board[8] == marker:
        return True
    elif board[3] == board[6] == board[9] == marker:
        return True
    elif board[1] == board[5] == board[9] == marker:
        return True
    elif board[3] == board[5] == board[7] == marker:
        return True
    else:
        return False


def space_check(board, position):
    return board[position] == " "


def full_board_check(board):
    mark = 0
    for i in board:
        if i is "X" or "O":
            mark += 1
    if mark is 9:
        return True
    else:
        return False


def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def player_choice(board):
    # entering the position
    position = int(input("Please enter the position: "))

    if space_check(board, position):
        return position
    else:
        return -1

# checking id player wants to restart the game
def replay():
    replay = input("Wanna replay? Y/n: ")
    if replay is "Y" or "y":
        return True
    else:
        return False


#starting the game
def play():
    print("Welcome to Tic Tac Toe Game")
    while True:
        # our board
        board = [" "]*10

        player1, player2 = player_input()

        turn = choose_first()
        print(turn + ' will go first')

        play_game = input("Ready to play? Enter 'Y' for yes: ")
        if play_game.lower()[0] == 'y':
            game_on = True
        else:
            game_on = False

        while game_on:
            if turn == "Player 1":

                display_board(board)
                position = player_choice(board)
                place_marker(board, player1, position)

                if win_check(board, player1):
                    display_board(board)
                    print("Congratulations you have won the game!")
                    game_on = False
                else:
                    if full_board_check(board):
                        display_board(board)
                        print('The game is a draw!')
                    else:
                        turn = "Player 2"
            else:
                display_board(board)
                position = player_choice(board)
                place_marker(board, player2, position)

                if win_check(board, player2):
                    display_board(board)
                    print("Congratulations you have won the game!")
                    game_on = False
                else:
                    if full_board_check(board):
                        display_board(board)
                        print('The game is a draw!')
                    else:
                        turn = "Player 1"

        if replay():
           break

play()

