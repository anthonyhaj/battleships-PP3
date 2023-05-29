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

def validate_coordinate(coordinate):
           """
    Validate the target coordinate input.
        coordinate (str): The target coordinate to validate.
        Returns True if the coordinate is valid, False otherwise.
    """
    # Checks if the coordinate has the correct length
    if len(coordinate) != 2:
        return False
    # Extracts the column and row values from the coordinate
    col = ord(coordinate[0]) - ord('A')
    try:
        row = int(coordinate[1:]) - 1
    except ValueError:
        # If the row value is not a valid integer, the coordinate is invalid
        return False
    # Checks if the column and row values are within the board boundaries
    return 0 <= col < board_size and 0 <= row < board_size

def place_ship(board, ship_name, ship_size):
    """
    Places a ship on the board with input validation.
        board (list): The game board to place the ship on.
        ship_name (str): The name of the ship.
        ship_size (int): The size of the ship.
    """
    print(f'Placing {ship_name} ({ship_size} cells)')
    # Gets the starting coordinate from the user
    while True:
        coords = input('Enter starting coordinate (e.g., A1): ').upper()
        # Validates the coordinate
        if not validate_coordinate(coords):
            print('Invalid coordinate. Please enter a valid starting coordinate.')
            continue
        # Gets the direction from the user
        direction = input('Enter direction (H for horizontal, V for vertical): ').upper()

        col = ord(coords[0]) - ord('A')
        row = int(coords[1:]) - 1
        # Checks if the horizontal placement is valid
        if direction == 'H' and col + ship_size <= board_size:
            if all(board[row][col+i] == empty_cell for i in range(ship_size)):
                # Places the ship horizontally on the board
                for i in range(ship_size):
                    board[row][col+i] = ship_cell
                break
            else:
                print('Invalid placement. Ships overlap.')
        # Checks if the vertical placement is valid        
        elif direction == 'V' and row + ship_size <= board_size:
            if all(board[row+i][col] == empty_cell for i in range(ship_size)):
                # Places the ship vertically on the board
                for i in range(ship_size):
                    board[row+i][col] = ship_cell
                break
            else:
                print('Invalid placement. Ships overlap.')
        else:
            print('Invalid placement. Ship goes out of bounds.')


