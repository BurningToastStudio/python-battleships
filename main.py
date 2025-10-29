# Max Martin - Y10CSC
from unittest import case

# grid will be stored as 2d array
grid = []

GRID_SIZE = 10
# TODO: support larger grid sizes
LETTERS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

CELL_EMPTY = ""
CELL_HAS_SHIP = "o"
CELL_HIT = "x"
CELL_MISS = "."

last_input_coordinate = None


def setup_grid():
    # create 2d array
    for i in range(GRID_SIZE):
        row = []  # create a row
        for j in range(GRID_SIZE):
            row.append(CELL_EMPTY)  # put empty cells into that row
        grid.append(row)  # add the row with empty cells to the grid

# will return a coordinate that is valid
# I call this "graceful error handling"
# the program should NEVER just crash for the user
def get_user_input():
    global last_input_coordinate
    coordinate = input("Enter the coordinate (e.g. a8): ")

    # clean the input
    coordinate = coordinate.strip().upper()
    last_input_coordinate = coordinate # save the cord for future reference

    # try split cord into a row and coll
    try:
        row_as_letter = str(coordinate[0])
        # converted to a number
        row = convert_letter_to_number(row_as_letter)
        # :1 means everything after the first character
        # do this so it can store column "10"
        column = int(coordinate[1:])
        # check that the column and row are in range
        # check more than 1
        # check less than grid_size
        if column < 1 or column > GRID_SIZE:
            raise ValueError
        if row < 1 or row > GRID_SIZE:
            raise ValueError

    except ValueError:
        print("Invalid coordinate")
        last_input_coordinate = None # cord was invalid, so clear
        return get_user_input() # get user input again

    return row, column

# rather than doing logic on the letter, just convert to the row number
def convert_letter_to_number(row):
    try:
        # get the index of the row letter in LETTERS
        # add one because lists start at 0 but my rows will start at 1
        row_as_number = LETTERS.index(row) + 1
    except ValueError:
        print(f"Invalid row: {row}")
        return get_user_input() # get user input again
    return row_as_number

def play_move(row, column):
    print(f"making move: {last_input_coordinate}")

    # -1 because index starts at 0
    cell = grid[row - 1][column - 1]

    if cell == CELL_HIT:
        print("already hit cell")
    elif cell == CELL_MISS:
        print("already miss cell")
    elif cell == CELL_HAS_SHIP:
        grid[row - 1][column - 1] = CELL_HIT
        print("HIT")
    elif cell == CELL_EMPTY:
        grid[row - 1][column - 1] = CELL_MISS
        print("MISS")
    else:
        print("invalid cell")

    return

# run
def print_grid():
    for row in grid:
        print(row)

def main():
    setup_grid()
    game_running = True
    while game_running:
        row, column = get_user_input()
        play_move(row, column)

main()