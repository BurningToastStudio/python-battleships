# Max Martin - Y10CSC
import tkinter as tk

root = tk.Tk()
root.geometry("500x500")
root.title("Battleships")
#root.resizable(False, False)


# grid will be stored as 2d array
grid = []
buttons = []  # 2D list to store all button references

# have 1 extra because it includes the letter and number headings
GRID_SIZE = 10
# TODO: support larger grid sizes
LETTERS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

# how the cell states are stored in the grid
GRID_CELL_EMPTY = ""
GRID_CELL_HAS_SHIP = "o"
GRID_CELL_HIT = "x"
GRID_CELL_MISS = "."

# how the cell states are stored visually on the buttons
BUTTON_CELL_EMPTY = ""
#BUTTON_CELL_HAS_SHIP = "o"
BUTTON_CELL_HIT = "X"
BUTTON_CELL_MISS = "O"

BUTTON_CELL_FONT = "Arial", 50
BUTTON_CELL_WIDTH = 4
BUTTON_CELL_HEIGHT = 2

LABEL_CELL_FONT = "Arial", 10, "bold"
LABEL_CELL_WIDTH = 4
LABEL_CELL_HEIGHT = 2

GRID_PADDING = (0, 0)

last_input_coordinate = None


def setup_grid():
    # create 2d array
    for i in range(GRID_SIZE):
        row = []  # create a row
        for j in range(GRID_SIZE):
            row.append(GRID_CELL_EMPTY)  # put empty cells into that row
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
    elif cell == GRID_CELL_EMPTY:
        grid[row - 1][column - 1] = CELL_MISS
        print("MISS")
    else:
        print("invalid cell")

    return

# run
def print_grid():
    for row in grid:
        print(row)

def on_button_cell_clicked(row, col):
    pass

def setup_grid_buttons():
    # create frame to store the buttons
    board_frame = tk.Frame(root)
    # relx / rely is relative x and relative y (relative to window size)
    # 0 - 1 is from edge to edge
    # using 0.5 makes it centered
    board_frame.place(relx=0.5, rely=0.5, anchor="center")  # center the frame

    for row in range(GRID_SIZE):
        row_buttons = []
        for col in range(GRID_SIZE):
            button = tk.Button(
                board_frame,
                text=BUTTON_CELL_EMPTY,
                width=BUTTON_CELL_WIDTH,
                height=BUTTON_CELL_HEIGHT,
                command=lambda r=row, c=col: on_button_cell_clicked(r, c)
            )
            button.grid(row=row + 1, column=col + 1, padx=GRID_PADDING[0], pady=GRID_PADDING[1])
            row_buttons.append(button)
        buttons.append(row_buttons)

        # add number headers (1–10)
        for col in range(GRID_SIZE):
            label = tk.Label(
                board_frame,
                text=str(col + 1),
                width=LABEL_CELL_WIDTH,
                height=LABEL_CELL_HEIGHT,
                font=LABEL_CELL_FONT
            )
            label.grid(row=0, column=col + 1, padx=GRID_PADDING[0], pady=GRID_PADDING[1])

        # add letter headers (A–J)
        for row in range(GRID_SIZE):
            label = tk.Label(
                board_frame,
                text=LETTERS[row],
                width=LABEL_CELL_WIDTH,
                height=LABEL_CELL_HEIGHT,
                font=LABEL_CELL_FONT
            )
            label.grid(row=row + 1, column=0, padx=GRID_PADDING[0], pady=GRID_PADDING[1])


setup_grid_buttons()
tk.mainloop()