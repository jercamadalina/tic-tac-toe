import os
import time


def main_title():
    os.system('clear')
    print("""              ######## ####  ######
                 ##     ##  ##    ##
                 ##     ##  ##
                 ##     ##  ##
                 ##     ##  ##
                 ##     ##  ##    ##
                 ##    ####  ######   """)
    time.sleep(.75)
    os.system('clear')
    print("""              ######## ####  ######          ########    ###     ######
                 ##     ##  ##    ##            ##      ## ##   ##    ##
                 ##     ##  ##                  ##     ##   ##  ##
                 ##     ##  ##       #######    ##    ##     ## ##
                 ##     ##  ##                  ##    ######### ##
                 ##     ##  ##    ##            ##    ##     ## ##    ##
                 ##    ####  ######             ##    ##     ##  ######  """)
    time.sleep(1)
    os.system('clear')
    print("""              ######## ####  ######          ########    ###     ######          ########  #######  ########
                 ##     ##  ##    ##            ##      ## ##   ##    ##            ##    ##     ## ##
                 ##     ##  ##                  ##     ##   ##  ##                  ##    ##     ## ##
                 ##     ##  ##       #######    ##    ##     ## ##       #######    ##    ##     ## ######
                 ##     ##  ##                  ##    ######### ##                  ##    ##     ## ##
                 ##     ##  ##    ##            ##    ##     ## ##    ##            ##    ##     ## ##
                 ##    ####  ######             ##    ##     ##  ######             ##     #######  ######## """)


def init_board():
    board = []
    for i in range(3):
        inner_list = []
        for j in range(3):
            inner_list.append('.')
        board.append(inner_list)
    return board


def get_move(board, player):
    coordinate_list = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
    coordinate = input('Please enter coordinates:  ')
    if coordinate not in coordinate_list:
        print("Input is wrong")
        return get_move(board, player)
    else:
        coordinate_dictionary = {'A': 0, 'B': 1,
                                 'C': 2, '1': 0, '2': 1, '3': 2}
        row = coordinate_dictionary[coordinate[0]]
        col = coordinate_dictionary[coordinate[1]]
    if board[row][col] != '.':
        print('Location is taken')
        return get_move(board, player)
    else:
        return row, col


def mark(board, player, row, col):
    if board[row][col] == ".":
        if player == 1:
            board[row][col] = "X"
        elif player == 2:
            board[row][col] = "0"
    return


def has_won(board, player):
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != '.':
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != '.':
            return True
    if board[0][0] == board[1][1] == board[2][2] != '.':
        return True
    if board[2][0] == board[1][1] == board[0][2] != '.':
        return True
    return False


def is_full(board):
    for row in range(3):
        for col in range(3):
            if board[row][col] == ".":
                return False
    return True


def print_board(board):
    print(2*" " + "| 1 | 2 | 3 |")
    print("---------------")
    for x in range(len(board[0])):
        if x == 0:
            print("A | ", end="")
        elif x == 1:
            print("B | ", end="")
        elif x == 2:
            print("C | ", end="")
        else:
            None
        for i in range(len(board[0])):
            print('' + board[x][i], end=" | ")
        print()
        for i in range(len(board[0])):
            print("-----", end="")
        print()


def print_result(winner):
    if winner is None:
        input('It\'s tie.')
    else:
        input(f'\n\tWinner is {winner}!')


def tictactoe_game(mode='HUMAN-HUMAN'):
    if mode == 1:
        board = init_board()
    while not has_won(board, 1) and not has_won(board, 2) and not is_full(board):
        os.system('cls')
        print_board(board)
        row, col = get_move(board, 1)
        mark(board, 1, row, col)
        os.system('cls')
        print_board(board)
        if not has_won(board, 1) and not is_full(board):
            row, col = get_move(board, 2)
            mark(board, 2, row, col)
            print_board(board)

    if has_won(board, 1):
        winner = 1
    elif has_won(board, 2):
        winner = 2
    else:
        winner = 0
    print_result
    print("Have a nice day")


def main_menu():
    main_title()
    print('\n\n\n')
    print("1. Human  vs.  Human".center(120))
    print('\n')
    print("Wanna play a game or you're too scared ? 'Quit':".center(120))
    print()

    mode = input(''.center(60)).lower()
    if mode == 'quit':
        exit()
    elif mode == 1 or 2:
        tictactoe_game(int(mode))


if __name__ == '__main__':
    main_menu()
