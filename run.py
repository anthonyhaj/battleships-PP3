# BattleShips Game

# Imports
import random

# Game board size
board_size = 10

# Constansts for cell states
empty_cell = ' '
ship_cell = 'O'
hit_cell = 'X'
miss_cell = '-'

# Ship sizes 
ship_sizes = {'Carrier': 5, 'Battleship': 4, 'Cruiser': 3, 'Submarine': 3, 'Destroyer': 2}

# Initialize the game boards for player and computer
player_board = [[empty_cell] * board_size for _ in range(board_size)]
computer_board = [[empty_cell] * board_size for _ in range(board_size)]

# Function to display the game board
def display_board(board, hide_ships=False):
    """
        Displays the game board.
        hide_ships: Whether to hide the ships on the board.
    """
    print('   ' + ' '.join(chr(ord('A') + i) for i in range(board_size)))
    for row in range(board_size):
        print(f'{row + 1:2d} ', end='')
        for col in range(board_size):
            cell = board[row][col]
            if cell == hit_cell or cell == miss_cell:
                print(cell + ' ', end='')
            elif cell == empty_cell:
                print(empty_cell + ' ', end='')
            elif hide_ships and cell == ship_cell:
                print(empty_cell + ' ', end='')
            else:
                print(cell + ' ', end='')
        print()