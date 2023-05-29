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
    # Print column labels
    print('   ' + ' '.join(chr(ord('A') + i) for i in range(board_size)))
    for row in range(board_size):
        # Print row number
        print(f'{row + 1:2d} ', end='')
        # Iterate over columns
        for col in range(board_size):
            cell = board[row][col]
            # Print cell contents based on its value
            if cell == hit_cell or cell == miss_cell:
                print(cell + ' ', end='')
            elif cell == empty_cell:
                print(empty_cell + ' ', end='')
            elif hide_ships and cell == ship_cell:
                print(empty_cell + ' ', end='')
            else:
                print(cell + ' ', end='')
        # Move to the next line after printing all cells in the row
        print()

# Function to validate target coordinate input
def validate_coordinate(coordinate):
           """
    Validate the target coordinate input.
    coordinate (str): The target coordinate to validate.
    Returns True if the coordinate is valid, False otherwise.
    """
    if len(coordinate) != 2:
        return False

    col = ord(coordinate[0]) - ord('A')
    try:
        row = int(coordinate[1:]) - 1
    except ValueError:
        return False

    return 0 <= col < board_size and 0 <= row < board_size