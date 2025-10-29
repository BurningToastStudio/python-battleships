# Max Martin - Y10CSC

# grid will be stored as 2d array
grid = []

GRID_SIZE = 10
# TODO: support larger grid sizes
LETTERS = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]

CELL_EMPTY = ""
CELL_HAS_SHIP = "o"
CELL_HIT = "x"
CELL_MISS = "."


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
    coordinate = input("Enter the coordinate (e.g. a8): ")

    # clean the input
    coordinate = coordinate.strip().lower()

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
        return get_user_input() # get user input again

    print(row, column)
    return row, column

# rather than doing logic on the letter, just convert to the row number
def convert_letter_to_number(row):
    try:
        # get the index of the row letter in LETTERS
        # add one because lists start at 0 but my rows will start at 1
        row_as_number = LETTERS.index(row) + 1
    except ValueError:
        print("Invalid row, grid size may be to big")
        return get_user_input() # get user input again
    return row_as_number

def check_valid_move(row, column):
    pass

# run
def print_grid():
    for row in grid:
        print(row)

setup_grid()
print_grid()
get_user_input()